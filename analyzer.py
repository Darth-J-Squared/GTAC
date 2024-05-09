import sys
import copy

def main():
    #take user selection for which graph
    to_open = input("Select Graph 1 ,2 , 3, or 4.")
    match to_open: #switch case to pull up the right file
        case '1':
            file = open("./unconnected/unconnected.txt", "r")
        case '2':
            file = open("./only_connected/connected.txt", "r")
        case '3':
            file = open("./Euler_Cycle/cycle.txt", "r")
        case '4':
            file = open("./Euler_Path/path.txt", "r")

    graph = []
    for line in file:
        graph.append([int(x) for x in line.split(",")[0:-1]])   #pulls each line into a list, throws out the newline character

    print("Testing for a connected graph:")
    if connected(graph): #starts checking in order for the different attributes
        print("The graph is fully connected.")
    else:
        print("The graph is not fully connected. Therefore there is no Euler Cycle or Path. Goodbye!")
        sys.exit()
    print("Testing if there is a Euler Cycle:")
    if hascycle(graph): #connected returns bool so you can use in an IF statement
        print("Conditions met for Euler Cycle.\nCalculating...")
        route = findcycle(graph) #hands it the graph, then takes back a list of instructions
        print("Cycle found! Here is the route:")
        print(route)
        print("This Cycle is also a Euler Path.\nThat is all, goodbye!")
        sys.exit()
    else:
        print("There is no Euler Cycle present in the graph.\nChecking for Euler Path:")
        path, start = haspath(graph) #since the process to test for a path existing can easily choose a starting node, we take back a bool and a node index
        if (path): #path is the bool that says if it exists or not
            print("Conditions met for Euler Path.\nCalculating...")
            route = findcycle(graph, start) #calls the same findcycle function, but provides a specific starting node, namely an odd one
            print("Path found! Here is the route:")
            print(route)
            print("We have shown that while there is no Euler Cycle, there is still a Euler Path.\nThat is all, goodbye!")
            sys.exit()
        else:
           print("Unfortunately, there is no Euler Path either. That is all, goodbye!")
           sys.exit()

def connected(graph, start=0, end="null"): 
#takes a graph to be tested, and defaults start to node 1 and end as nothing.
#this is important because we can dynamically use the function multiple times.
#if we want to check for connection to every node we only pass the graph
#if we want to test for bridge, we pass the nodes and a graph without the "bridge"
    size = len(graph[0]) #checks how many nodes in our graph
    reached = [0 for x in range(size)] #initializes a list of 0s for every node
    visited = [0 for x in range(size)]
    reached[start] = 1 #seeds it by saying we have reached the starting node
    to_check = [start] #seeds where to go next by saying we need to look at the starting node's children
    while to_check: #when no more nodes to check, we have no routes left to check
        node = to_check.pop(0) #takes out the first node in the list
        visited[node] = 1 #says we have visited it
        for index, connection in enumerate(graph[node]): #pulls both the index of the node, as well as the connection list
            if index == end and connection: #checks for if this is our end node in the bridge case, returns true if so
                return True
            elif connection and not reached[index]: #checks if we have a connection to a node we still need, this prevents loops
                reached[index] = 1 #says we have reached this new node
                to_check.append(index) #adds this node as another place to search from
    if all(reached): #we only reach this code once the above loop dies out. Then we see if we have reached all nodes. all checks for boolean values, but 1s count as true
        isconnected = True
    else:
        isconnected = False
    return isconnected
    
def hascycle(graph):
    for node in graph:# pretty simple, adds up connections of a given vertex and sees if it's even or not
        if (sum(node) % 2 != 0):
            return False
    return True

def haspath(graph):
    odd_count = 0 #similar to the last function, checks for if there are only 2 odd nodes, with the addition of storing which node it is to be used later
    for index, node in enumerate(graph):
        if (sum(node) % 2 != 0):
            odd_count += 1
            start = index
    if odd_count != 2:
        return False, 0
    return True, start

def findcycle(graph, start=0):#defaults start to 0, so we can call it with just a graph to find a euler cycle
    route = []
    dad = start
    children = findchildren(graph, start)#seeds the loop with the children of the starting node
    while children:
        if len(children) == 1:#if we only have one option left, we must take it, whether it is a bridge or not
            graph[dad][children[0]] = 0
            graph[children[0]][dad] = 0#this is effectively deleting a edge from the graph
            route.append("%s=>%s" % (dad + 1, children[0] + 1))#this adds our new connection to our final route. It's +1 to make the nodes start at 1, since humans are weird ¯\_(ツ)_/¯
            dad = children[0] #makes the next loop have the child as dad
            children = findchildren(graph, children[0]) #finds and seeds the children for the new dad
            continue
        bridge_test = children.pop(0) #this code runs if we have multiple options
        test_graph = copy.deepcopy(graph) #we create a new graph. copy.deepcopy makes sure we get a brand new clone of the original graph, not a reference to it. otherwise our tests destroy data
        test_graph[dad][bridge_test] = 0
        test_graph[bridge_test][dad] = 0 #removes the possible bridge from the test graph and sends it off to be tested for bridgeness
        if connected(test_graph, dad, bridge_test): #does the same process as for a connected graph, but only cares about finding a path between these two nodes
            children = [bridge_test]
    return route

def findchildren(graph, node):
    children = [] #simple function to find the "children" of a node
    for index, child in enumerate(graph[node]): #just loops through looking for connections
        if child == 1:
            children.append(index)
    return children

main()
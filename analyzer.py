import sys
import copy

def main():

    to_open = input("Select Graph 1 ,2 , 3, or 4.")

    match to_open:
        case '1':
            file = open("./unconnected/unconnected.txt", "r")
        case '2':
            file = open("./only_connected/connected.txt", "r")
        case '3':
            file = open("./Euler_Cycle/cycle.txt", "r")
        case '4':
            file = open("./Euler_Path/path.txt", "r")

    #file = open("./Euler_Cycle/cycle.txt", "r")

    graph = []
    for line in file:
        graph.append([int(x) for x in line.split(",")[0:-1]])


    print("Testing for a connected graph:")
    if connected(graph):
        print("The graph is fully connected.")
    else:
        print("The graph is not fully connected. Therefore there is no Euler Cycle or Path. Goodbye!")
        sys.exit()
    print("Testing if there is a Euler Cycle:")
    if hascycle(graph):
        print("Conditions met for Euler Cycle.\nCalculating...")
        route = findcycle(graph)
        print("Cycle found! Here is the route:")
        print(route)
        print("This Cycle is also a Euler Path.\nThat is all, goodbye!")
        sys.exit()
    else:
        print("There is no Euler Cycle present in the graph.\nChecking for Euler Path:")
        path, start = haspath(graph)
        if (path):
            print("Conditions met for Euler Path.\nCalculating...")
            route = findcycle(graph, start)
            print("Path found! Here is the route:")
            print(route)
            print("We have shown that while there is no Euler Cycle, there is still a Euler Path.\nThat is all, goodbye!")
            sys.exit()
        else:
           print("Unfortunately, there is no Euler Path either. That is all, goodbye!")
           sys.exit()

    file.close()

def connected(graph, start=0, end="null"):
    size = len(graph[0])
    reached = [0 for x in range(size)]
    visited = [0 for x in range(size)]
    reached[start] = 1
    to_check = [start]
    while to_check:
        node = to_check.pop(0)
        visited[node] = 1
        for index, connection in enumerate(graph[node]):
            if index == end and connection:
                return True
            elif connection and not reached[index]:
                reached[index] = 1
                to_check.append(index)
    if all(reached):
        isconnected = True
    else:
        isconnected = False
    return isconnected
    
def hascycle(graph):
    for node in graph:
        if (sum(node) % 2 != 0):
            return False
    return True

def haspath(graph):
    odd_count = 0
    for index, node in enumerate(graph):
        if (sum(node) % 2 != 0):
            odd_count += 1
            start = index
    if odd_count != 2:
        return False, 0
    return True, start

def findcycle(graph, start=0):
    route = []
    dad = start
    children = findchildren(graph, start)
    while children:
        if len(children) == 1:
            graph[dad][children[0]] = 0
            graph[children[0]][dad] = 0
            route.append("%s=>%s" % (dad + 1, children[0] + 1))
            dad = children[0]
            children = findchildren(graph, children[0])
            continue
        bridge_test = children.pop(0)
        test_graph = copy.deepcopy(graph)
        test_graph[dad][bridge_test] = 0
        test_graph[bridge_test][dad] = 0
        if connected(test_graph, dad, bridge_test):
            children = [bridge_test]
    return route

def findchildren(graph, node):
    children = []
    for index, child in enumerate(graph[node]):
        if child == 1:
            children.append(index)
    return children

main()
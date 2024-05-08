import sys

def main():

    file = open("./Euler_Cycle/cycle.txt", "r")

    graph = []
    for line in file:
        graph.append([int(x) for x in line.split(",")[0:-1]])

    print(graph)

    print("Testing for a connected graph:")
    if connected(graph):
        print("The graph is fully connected.")
    else:
        print("The graph is not fully connected. Therefore there is no Euler Cycle or Path. Goodbye!")
        sys.exit()
    print("Testing if there is a Euler Cycle:")
    if hascycle(graph):
        print("Conditions met for Euler Cycle.\nCalculating...")
        #route = findcycle(graph)
        #print("Cycle found! Here is the route:")
        #print(route)
        #print("This Cycle is also a Euler Path.\nThat is all, goodbye!")
        #sys.exit()
    else:
        print("There is no Euler Cycle present in the graph.\nChecking for Euler Path:")
        #if(haspath(graph):
        #   print("Conditions met for Euler Path.\nCalculating...")
        #   route = findpath(graph)
        #   print("Path found! Here is the route:")
        #   print(route)
        #   print("We have shown that while there is no Euler Cycle, there is still a Euler Path.\nThat is all, goodbye!")
        #   sys.exit()
        #else:
        #   print("Unfortunately, there is no Euler Path either. That is all, goodbye!")
        #   sys.exit()

    file.close()

def connected(graph):
    size = len(graph[0])
    reached = [0 for x in range(size)]
    visited = [0 for x in range(size)]
    print(reached)
    reached[0] = 1
    to_check = [0]
    while to_check:
        node = to_check.pop(0)
        visited[node] = 1
        for index, connection in enumerate(graph[node]):
            if connection and not reached[index]:
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
    for node in graph:
        if (sum(node) % 2 != 0):
            odd_count += 1
    if odd_count != 2:
        return False
    return True


 

main()

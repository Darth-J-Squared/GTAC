def main():

    file = open("graph_15.txt", "r")

    graph = []
    for line in file:
        graph.append([int(x) for x in line.split(",")[0:-1]])

    print(graph)

    print("Testing for a connected graph:")
    isconnected = connected(graph)
    if isconnected:
        print("The graph is fully connected.")
    else:
        print("The graph is not fully connected.")
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
    





main()

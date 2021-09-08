'''
Given different number of islands or different graphs of different sizes
we have to find the island/graph with the largest number of components
'''

graph = {
    0: [8,1,5],
    1: [0],
    5: [0,8],
    8: [0,5],
    2: [3,4],
    3: [2,4],
    4: [3,2]
    
}

def explore(graph, current_node, visited):
    
    if current_node in visited:
        return 0
    visited.add(current_node)
    nodes_visited = 1 # to count the nodes in the graph
    for neighbour in graph[current_node]:
        nodes_visited += explore(graph, neighbour, visited)
        

    return nodes_visited

def largestConnectedComponents(graph):
    # Creating a set to keep track of the visited nodes
    visited = set()
    largest = 0
    count = 0
    for node in graph:
        count = explore(graph, node, visited)

        if count >= largest:
            largest = count

    return largest

assert largestConnectedComponents(graph) == 4 
print(largestConnectedComponents(graph))

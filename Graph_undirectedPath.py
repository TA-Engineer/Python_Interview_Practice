'''
This is the source code for undirected graph problems 

Complexity
n = # of node
e = # of edges

Time: O(e)
Space: O(n)
'''

edges = [
    ['i','j'],
    ['k','i'],
    # ["k","j"],
    ['m','k'],
    ['k','l'],
    ['o','n']
    ]

    # here every pair in the edge list shows a connection in the graph
    
# Converting edges into adjency list

# Note: Since the graphs are connected whenever you insert a key for a connection
# insert that key in the inverse connection


def buildGraph(edges):
    graph = {}

    for edge in edges:
        a, b = edge[0], edge[1]

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph

# graph = {
#     "i": ["j","k"],
#     "j": ["i","k"],
#     "k": ["i","m","l","j"],
#     "m": ["k"],
#     "l": ["k"],
#     "o": ["n"],
#     "n": ["o"]
# }
# There is a cycle of i j and k Also between o and n
# So we will use a check to see if we have visited a node before

def hasPath(graph, source, dest, visited):    
    if (source == dest): return True # check if source is equal to desstination
    if source in visited: return False # check if we have visited this node to avoid cycle

    visited.add(source) # if not then add that node to our set list
    for neighbour in graph[source]:
        if hasPath(graph, neighbour, dest, visited) == True:
            return True

    return False

def undirectedPath(edges, nodeA, nodeB):

    graph = buildGraph(edges)
    # print(graph)
    x = set() # this set will keep a check if we have visited a node. We will pass
    return hasPath(graph, nodeA, nodeB, x)




src = 'i'
dest = 'l'

print(undirectedPath(edges, src, dest))

# NOW IMPLEMENTING A TRAVERSAL

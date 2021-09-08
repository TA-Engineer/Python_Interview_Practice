'''
In this list we are finding the shortest path for between our source and destination

Will use Breath first serach and we will count the path length which will be returned

'''
 
 
edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]

# First converting our edge list to a graph using a function

def buildGraph(edges):
    graph = {}
    for edge in edges:
        
        if edge[0] not in graph: 
            graph[edge[0]] = []
            
        graph[edge[0]].append(edge[1])
        
        if edge[1] not in graph:
            graph[edge[1]] = []
            
        graph[edge[1]].append(edge[0])
    
    return graph

def explore(graph, current_node, visited):
    pass
    

def shortestPath(edges, source, dest):
    graph = buildGraph(edges)
    # print(graph)
    
    queue = [[source,0]]
    visited = set(source)
    
    while len(queue) > 0:
        current = queue.pop(0)
        # print(current)
        
        if current[0] == dest:
            return current[1]
    
        for node in graph[current[0]]:
            if node not in visited:
                queue.append([node,current[1]+1])
                visited.add(node)
            
        

    return "Not Connected"
    



    # explore(graph, source, dest)



print(shortestPath(edges, 'w', 'z'))
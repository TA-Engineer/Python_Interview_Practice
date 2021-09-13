'''
This is the code for acyclic graphs: no cycles.
Here we can do depth first or breath first search however,
what we do is we look at the source node to destination node
if we fine a path we return True and if we do not find a path we return False
'''
 
 
def hasPath_depth(graph, src, dest):
    if src == dest:
        return True
        
    # If source is not equal to the path then we have to keep looking
    for neighbour in graph[src]:
        if hasPath(graph, neighbour, dest) == True:
            
            return True

    return False
def hasPath_Breath(graph, source, dest):
    queue = [source]
    while len(queue) > 0:
        current = queue.pop(0)
        if current == dest:
            return True
        for neighbour in graph[current]:
            queue.append(neighbour)

    return False


graph ={
    'f': ['g','i'],
    'g': ['h'],
    'h': [],
    'i': ['g','k'],
    'j': ['i'],
    'k': []
}



print(hasPath_Breath(graph, 'f', 'k'))
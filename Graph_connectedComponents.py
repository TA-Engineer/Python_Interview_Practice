'''
In this code we will be counting how many nodes of the graph are connected

'''



# This is the explore function that will explore depth wise each node

def explore(graph, current_node, visited):
    
    if current_node in visited:
        return False
    else:
        visited.add(current_node)

    for neighbour in graph[current_node]:
        explore(graph, neighbour, visited)
    
    # This is to check we have visited all of the nodes in the neighbour calls

    return True


# define a funciton that takes in the graph 

def connectedComponentCount(graph):
    # now we will search through each node
    # we are given a dictionary therefore we will iterate through the keys.
    
    visited = set() # creating a visited set to check if we have visited a node before or not
    
    count = 0 # checking the components count variable

    for node in graph:
        if explore(graph, node, visited): 
            # Once we finsh visiting all the components of the graph we increase count
            count += 1

    return count



graph = {
    0: [8,1,5],
    1: [0],
    5: [0,8],
    8: [0,5],
    2: [3,4],
    3: [2,4],
    4: [3,2]
    
}


assert connectedComponentCount(graph)== 2 
print("Number of connected components are: ", connectedComponentCount(graph))
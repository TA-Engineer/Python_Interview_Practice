'''
This is my practice file where I have practiced graphs
'''

# first create a basic graph for practice

#Creating an adjacency list

graph = {
    'a' : ['c', 'b'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : []
}

# Creating a depth first array function
def depthFirstPrint(graph,source):
    stack = [source]

    while(len(stack)>0):
        current = stack[-1]
        stack.pop()
        print(current)

        for neighbour in graph[current]:
            stack.append(neighbour)


# Testing out the code
# depthFirstPrint(graph, 'a')# abdfce


# Solving recursively

def depthFirstPrintRecursive(graph, source):

    print(source)
    for neighbour in graph[source]:
        depthFirstPrintRecursive(graph,neighbour)

# Recursive output
# depthFirstPrintRecursive(graph, 'a') # acebdf




# Solving Breath First solving iteratively

def breathFirstPrint(graph, source):
    queue = [source]

    while (len(queue)>0):
        front = queue.pop(0)
        print(front)
        for neighbour in graph[front]:
            queue.append(neighbour)


breathFirstPrint(graph, 'a')

''' note the structure of the code in both cases is identical its just we need to implement
stack vs queue'''
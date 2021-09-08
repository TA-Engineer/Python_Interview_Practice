grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]


def explore(grid, row, col, visited):

    rowinbound = (row>=0 and row <len(grid))
    colinbound = (col>=0 and col <len(grid[0]))

    if not rowinbound or not colinbound:return 0
    if grid[row][col] == 'W': return 0

    pos = str(row)+','+str(col)
    if pos in visited: return 0
    visited.add(pos)

    length = 1

    length += explore(grid, row-1, col, visited)
    length += explore(grid, row+1, col, visited)
    length += explore(grid, row, col-1, visited)
    length += explore(grid, row, col+1, visited)
    
    return length


def minimumIslandCount(grid):

    visited = set()
    minSize = float('inf')
    for row in range(0,len(grid)):
        for col in range(0,len(grid[0])):
            size = (explore (grid, row, col, visited))

            if size < minSize and size >0:
                minSize = size
    
    return minSize
print(minimumIslandCount(grid))
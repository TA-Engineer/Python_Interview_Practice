grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

# islandCount(grid); // -> 3

def explore(grid, row, col, visited):
    
    
    rowInbound = (row >= 0 and row < len(grid))
    colInbound = (col >= 0 and col < len(grid[0]))

    if not rowInbound or not colInbound: return False
    if grid[row][col] == 'W': return False

    position = str(row) +','+str(col)
    if position in visited: return False
    
    visited.add(position)

    

    explore(grid, row+1, col, visited)
    explore(grid, row-1, col, visited)
    explore(grid, row, col-1, visited)
    explore(grid, row, col+1, visited)

    return True



def islandCount(grid):

    visited = set()
    count = 0

    for row in range(0,len(grid)):
        for col in range(0,len(grid[0])):
            if explore(grid, row, col, visited) == True:
                print(visited)
                count += 1

    return count

print(islandCount(grid))
           


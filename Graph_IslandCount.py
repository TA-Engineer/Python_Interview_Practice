grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
];

# islandCount(grid); // -> 3

def explore(grid, row, col, visited):
    
    queue = [[row,col]]
    
    position = str(row) +','+str(col)
    # if position in visited:
    #     return
    visited.add(position)

    while len(queue) > 0:
        current = queue.pop(0)
        row = current[0]
        col = current[1]
    
    if row > 0:
        check  = grid[row-1][col]
        position = str(row-1)+','+str(col)
        
        if check == 'L'and position not in visited:
            visited.add(position)
            queue.append([row-1,col])

    if row < len(grid)-1:
        check = grid[row+1][col]
        position = str(row+1)+','+str(col)

        if check == 'L' and str((row+1,col)) not in visited:
            visited.add(position)
            queue.append([row+1,col])

    
    if col > 0:
        check = grid[row][col-1]
        position = str(row)+','+str(col-1)
        
        if check == 'L'and position not in visited:
            visited.add(position)
            queue.append([row,col-1])

    if col < (len(grid[0])-1):
        check = grid[row][col+1]
        position = str(row)+','+str(col+1)

        if check == 'L'and position not in visited:
            visited.add(position)
            queue.append([row,col+1])

    return visited


# def islandCount(grid):

#     visited = set()
#     count = 0

#     for row in range(0,len(grid)):
#         for col in range(0,len(grid[0])):
            
#             if grid[row][col] == 'L' and str((row,col)) not in visited:
#                 count +=1                
#                 visited.update(explore(grid, row, col, visited))
    
    return count

def islandCount(grid):

    visited = set()
    count = 0

    for row in range(0,len(grid)):
        for col in range(0,len(grid[0])):
            explore(grid, row, col, visited)
            
            position = str(row)+','+str(col)

            if grid[row][col] == 'L' and position not in visited:
                count +=1                
                visited.update(explore(grid, row, col, visited))
    
    return count

print(islandCount(grid))
           


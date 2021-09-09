'''
In this code I solve the grid traveler problem

'''

def gridTraveler(m,n, memo = {}):
    pos = str(m)+','+str(n)
    if pos in memo: return memo[pos]
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    
    memo[pos] = (gridTraveler(m-1,n, memo))+gridTraveler(m,n-1, memo)

    return memo[pos]

    # return (gridTraveler(m-1,n))+gridTraveler(m,n-1)
    # # This is very slow when grid size increases




print(gridTraveler(1,1))
print(gridTraveler(2,3))
print(gridTraveler(3,2))
print(gridTraveler(3,3))
print(gridTraveler(18,18))
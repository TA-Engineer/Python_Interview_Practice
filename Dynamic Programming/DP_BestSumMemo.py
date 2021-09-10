''''
Write a func bestSum(targetSum, numbers) that takes in a targetSum and an array of numbers as arguments.

The func should return an array containing the shortest combination of numbers that add up to exactly
the targetSum.

'''

def bestSum(targetSum, numbers, memo = dict()):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None

    shortestCombination = None

    for num in numbers:
        remainder = targetSum - num
        remainderSum = bestSum(remainder, numbers)    
        if remainderSum != None:
            combination = remainderSum + [num]
            if shortestCombination == None or len(shortestCombination) > len(combination):
                shortestCombination = combination
                
    memo[targetSum] =  shortestCombination
    return shortestCombination
 
# now checking some test cases
memo = {}
print( bestSum(7, [3, 3, 4, 7], memo))
memo = {}
print( bestSum(8, [2,3,5], memo))
memo = {}
print( bestSum(8, [1, 4, 5], memo))
memo = {}
print( bestSum(300, [1, 2, 5, 25,100], memo))
            


'''
Output:
[7]
[5, 3]
[5, 3]
[100, 100, 100]

Looking at time complexity

m = target Sum
n = numbers length

Runtime
Brute Force:
Time: O(n^m * m) times m as we linearly copy all the values
Space: O(m^2)


Memoized
Time: (m^2*n)
Space: (m^2)
'''
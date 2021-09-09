'''
Write a function cansum (targetSUm, numbers) that takes in a target sum and an array of numbers as argument

The funciton should return a boolean indicating whether or not it is possible to generate the targetSum
using numbers from the array.

You may use an element of the array as many times as needed

You may assume that all input numbers are nonnegative
'''

# Example: CanSum(7, [5, 3, 4, 7]) return True
# Example: CanSum(7, [2, 4]) return False

def canSum(targetSum, numbers, memo={}):
    # Base case
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return True
    if targetSum < 0: return False
    
    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers, memo) == True:
            memo[targetSum] = True
            return True

        # memo[remainder] = canSum(remainder,numbers, memo)
        # if  memo[remainder]== True:
        #     return True

    memo[targetSum] = False # note remove this as well if implementing green
    return False

memo = {}
print( canSum(7, [2, 4], memo)) # false
memo = {}
print( canSum(7, [2, 3], memo)) # True
memo = {}
print( canSum(7, [5, 3, 4, 7], memo)) #True
memo = {}
print( canSum(8, [2, 3, 5], memo)) # True
memo = {}
print( canSum(300, [7, 14], memo)) # False

# The issue with the code below is that the memo object is transfering from one call to another.

# print( canSum(7, [2, 4])) # false
# print( canSum(7, [2, 3])) # True
# print( canSum(7, [5, 3, 4, 7])) #True
# print( canSum(8, [2, 3, 5])) # True
# print( canSum(300, [7, 14])) # False
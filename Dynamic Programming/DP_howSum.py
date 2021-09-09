'''
Write a func howsum(targetSum, numbers) that takes in a targetSum and an array of nums as arguments

The func. should return an array containing any cmbinations of elements that add up to exactly the targetSum.
If there is no combination that adds up to the targetSum, then return null.

If there are multiple combinations possible, you may return any single one.
'''
# example: howSum( 7, [5, 3, 4, 7]) -> [7] or [3,4] either is correct
# exmaple: howSum(7, [2, 4]) -> return null
# example: howSum(0, [1,2,3]) -> return [] empty array


def howSum(targetSum, numbers, memo = {}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None

    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers, memo)
        
        if remainderResult != None:
            memo[targetSum] = remainderResult + [num]
            return memo[targetSum]

    memo[targetSum] = None
    return None



memo = {}
print(howSum(7, [ 2, 3], memo ))
memo = {}
print(howSum(7, [5, 3, 4, 7], memo))
memo = {}
print(howSum(7, [2, 4], memo ))
memo = {}
print(howSum(8, [2, 3, 5], memo ))
memo = {}
print(howSum(300, [7, 14], memo ))
'''
Write a function canConstruct(target, wordBank) that accepts a target
string and an array of strings.

The function should returna  boolean indicating whether or not the 'target'
can be constructed by concatenating elements of the 'wordBank' array.

You may reuse elements of 'wordBank' as many times as needed.
'''

def canConstruct(target, wordBank, memo = {}):
    if target in memo: return memo[target]
    if target == '': return True

    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]

            if canConstruct(suffix, wordBank, memo) == True:
                memo[suffix] = True
                return True



    memo[target] = False
    return False


memo= {}
print( canConstruct("abcdef", ["ab","abc", "cd", "def", "abcd" ]))
# True

print( canConstruct( " skatebaord", ['bo', 'rd', 'ate', "t","ska", "sk", "boar"]))
# False

memo= {}
print(canConstruct("enterapotentpot", ['a', 'p', 'ent', 'enter', 'ot', 'o', 't' ] ))
# True

memo= {}
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeeee",
    "eeeeee"
])) # False


''''
Output:



Time complexity

 m = target.length
 n = wordBank.length

Brute Force
Time O(n^m * m)
Space O(m^2)

Memoized:
Time: O(n*m^2)
Space: O(m^2)
'''
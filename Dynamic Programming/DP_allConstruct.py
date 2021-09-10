'''
Write a function allConstruct(target, wordBank) that accepts a target
string and an array of strings.

The function should return a 2D array containing all of the ways that the
target can be constructed by concatenating elements of the wordBank array
Each element of that 2D arry should represent one combination that the target
word can be constructed.

You may reuse elements of 'wordBank' as many times as needed.
'''

def allConstruct(target, wordBank, memo = {}):
    if target in memo: return memo[target]
    if target == '': return [[]]
    results = []
    for word in wordBank:

        if target.find(word) ==0:
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix, wordBank, memo)
            
            targetWays = list(map(lambda x: [word] + x, suffixWays))
            # targetWays = [[word] + x for x in suffixWays]
            # print("     ",targetWays)
            results += targetWays
    # print(results)

    memo[target] = results
    return results



memo= {}
print( allConstruct("purple", ["purp", "p", "ur", "le", "purpl" ], memo))
# 2
memo= {}
print( allConstruct("abcdef", ["ab","abc", "cd", "def", "abcd",'ef','c' ], memo))
# 1
print( allConstruct( " skatebaord", ['bo', 'rd', 'ate', "t","ska", "sk", "boar"], memo))
# 0
memo= {}
# print(allConstruct("enterapotentpot", ['a', 'p', 'ent', 'enter', 'ot', 'o', 't' ] ))
# 4
memo= {}
print(allConstruct("aaaaaaaaaaaaaaaaaaaaaaz", [
    "a",
    "aa",
    "aaa",
    "aaaa",
    
], memo)) # 0


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
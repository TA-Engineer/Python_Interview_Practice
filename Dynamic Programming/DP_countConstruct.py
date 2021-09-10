'''
Write a function countConstruct(target, wordBank) that accepts a target
string and an array of strings.

The function should returna  boolean indicating whether or not the 'target'
can be constructed by concatenating elements of the 'wordBank' array.

You may reuse elements of 'wordBank' as many times as needed.
'''

def countConstruct(target, wordBank, memo = {}):
    if target in memo: return memo[target]
    if target == '': return 1

    count = 0
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]

            numways = countConstruct(suffix, wordBank, memo)
            count += numways
    
    memo[target] = count        
    return count



memo= {}
print( countConstruct("purple", ["purp", "p", "ur", "le", "purpl" ]))
# 2
memo= {}
print( countConstruct("abcdef", ["ab","abc", "cd", "def", "abcd" ]))
# 1
print( countConstruct( " skatebaord", ['bo', 'rd', 'ate', "t","ska", "sk", "boar"]))
# 0
memo= {}
print(countConstruct("enterapotentpot", ['a', 'p', 'ent', 'enter', 'ot', 'o', 't' ] ))
# 4
memo= {}
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeeee",
    "eeeeee"
])) # 0


''''
Output:
2
1
0
4
0


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
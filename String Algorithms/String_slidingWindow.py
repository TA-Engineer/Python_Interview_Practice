'''
Sliding Window

This is a pattern recognition algorithm where it takes an input T and
pattern P the code will go through the string T and find the 
location of P in T. 

The sliding window comes from the name as we will slide a window of length P
through T to find the pattern match. 
In addition please note when doing the loop through T we will only go till
T - P - 1 as when the window is as indexded after T-P the pattern length
will be out of index range.


Step:
- Define a function match that matches the characters
    - takes string A and B checks if they are equal
    - if len A != len B: return False
    - loop from 0 to A-1: check if a[i] != b[i] return False
    - When for loop is finished the string mateches so return True


- Define a func 'slidingWindow(targerString, Patterm)'
- Define en empty list to keep track of the indexes found
- Cal the length of the targetString and Pattern  strings
- Loop through the string in slidingwindow to see the pattern 
  matches or not.
        - the len of the loop should 0 to target-pattern
- send the targetString[i:i+len(P)-1] and pattern to matching func above
- if found append to index list else continue to next

- return the final list


'''
# Function to match any two strings
def match(stringA, stringB):
    
    # checking if the strings are equal in length
    if len(stringA) != len (stringB): return False
    
    
    # loop and check if the characters matches
    for i in range(0, len(stringA)):
    
        # if condition if matching fails at anypoint
        if stringA[i] != stringB[i]: return False
    
    # if no failure return True
    return True

# Sliding window function
def slidingWindow(targetString, pattern):
    
    indexFound = []
    targetLength = len(targetString)
    patternLength = len(pattern)

    for i in range(0, targetLength - patternLength):
        if match(targetString[i:i+patternLength], pattern) == True:            
            indexFound.append(i)

    return indexFound


print(slidingWindow("abcfgjafsdabcdfsdsdabc", 'abc'))
print(slidingWindow("coddddd hello, cod is cod and now jus c od co d", 'cod'))
print(slidingWindow("aaaaaaabaaaaaabaaaaabaaaa", 'b'))



'''
The running time of this algorithm is 
T = length of target string
P = length of pattern string

Time for sliding window: O(T*P)
Time for matching: O(P) caudse we are only looking at length of the string

'''
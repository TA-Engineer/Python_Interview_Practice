''''
Using Dynamic Programming code the Fib Sequence
'''
# WE will try solving this through recurssion
def fib(n):
    if n <=2:
        return 1
    return fib(n-1)+fib(n-2)

'''
Solving for a large number is a problem as that can take a long time and 
and additionally we are re entering a lot of the same number
so how can we reduce it?
'''
def fib_DP(n):

    fibs = [0,1]
    if n<=1: return fibs[n]
    for i in range(2,n+1):
        fibs.append(fibs[i-1]+fibs[i-2])
    return fibs[n]

print(fib_DP(50))


def fib_hash_DP(n, memo = {}):
    if n in memo: return memo[n]
    if n<=2 : return 1
    memo[n] = fib_hash_DP(n-1, memo) + fib_hash_DP(n-2, memo)
    return memo[n]

print(fib_hash_DP(50))

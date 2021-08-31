import math

'''
This is the code for linear search
We will solve it recursively

Function input arguments:
    A: is the array passed to be searched into
    low: is the lower bound of the array to be searched in
    high: is the upper bound of the array to be searched in
    key: the value we are looking for

RUNTIME: The runtime of Linear search is O(n) + c
         Where it depends where the value is located

'''

def LinearSearch(A, low, high, key):
    if high < low:
        return "Not Found"
    
    if A[low] == key:
        return low
    return LinearSearch(A, low+1, high, key)

# ITERATIVE VERSION

def LinearSearchIT(A, low, high, key):
    for i in range(low, high):
        if A[i] == key:
            return i
        
    return "Not Found"


'''
This code is for Binary Search
We will solve it recursively

Function input arguments:

    A: Array of SORTED VALUES (if values are not sorted write an input function)
    low: lower bound of the input array
    high: higher bound of the input array
    key: The value we are looking for

RUNTIME: the run time is O(log n)

IMP: We will solve this problem recursively
'''

def BinarySearch(A, low, high, key):
    
    # Checking the condition that the upper bound is high that the lower bound
    if high < low:
        return low -1
    
    # Calculating the center of the array
    mid = math.floor( low + ((high - low)/2))

    # Checking if the key is at mid point
    if A[mid] == key:
        return mid

    # Checking if the key is less than the mid point 
    elif key < A[mid]:
        # if true then we dont need to search in the upper half reducing values by 2
        return BinarySearch(A, low, mid-1, key)

    else:
        # here we assume after all checks the value lies above mid point index
        # Therefore, we search in the above part of the index.
        return BinarySearch(A, mid+1, high, key)

# ITERATIVE VERSION

def BinarySearchIT(A, low, high, key):
    
    # Checking the condition that the upper bound is high that the lower bound
    while high <= low:

        # Calculating the center of the array
        mid = math.floor( low + ((high - low)/2))

        # Checking if the key is at mid point
        if A[mid] == key:
            return mid

        # Checking if the key is less than the mid point 
        elif key < A[mid]:
            high = mid-1

        else:
            low = mid + 1
    return low - 1


'''
Now looking at the solution to multiply opoly nomials naive Solution

Arguments:
A: are the coefficients of poly A
B: are the coefficients of poly B
n: is the length of the 

'''

def Multpoly(A,B,n):
    product = []
    for i in range(0,2*n-1):
        product.append(0)
    
    for i in range(0, len(A)):
        for j in range(0, len(B)):
            product[i+j] = product[i+j] + A[i] + B[j]
    
    return product
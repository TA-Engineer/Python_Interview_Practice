'''
This file contains sorting algorithms
'''


# Selection Sort
'''
Steps for selection sort
1. First find the minimum value in the given array
2. Swap it with the first element in the array.
   After swapping the minum element becomes the first element in the array and stays there.
   Therefore, we can forget it and find a new element.
3. Repeat Step 1 & 2 with the remaining part of the array

Example:
[8,4,5,2,2] - select 2 as min and swap it with 8
[2,4,5,8,2] - select second 2 as min and swap it with 4; note looking at array from 4 to 2
[2,2,5,8,4] - select 4 as min and swap it with 5
[2,2,4,8,5] - select 5 as min swap it with 8
[2,2,4,5,8] - ARRAY IS SORTED this can be sent back

NOTE:
the runing time of this algorithm is only dependent on the size of the array and not on
the input elements.

Runtime of this algorithm is O(n^2) - cause there is a nested for loop


Argument in the function: A - is the input array to be sorted.
'''
def SelectionSort(A):
    
    for i in range(0, len(A)):
        minIndex = i
        for j in range(i+1, len(A)):
            
            # check if the current value of j is less than our initial index
            if A[j]<A[minIndex]:
                minIndex = j
        
        A[i], A[minIndex] = A[minIndex], A[i]





# Merge Sort

''''
Steps for merge sort Algorithm
1. Split the Array in two or more disjoint sub problems
2. Then solve each problem recursively
3. Then we merge the final results to get the final answer
        We do this by comparing the first values and then appending the smallest one to the 
        final array that will be returned.
        Do this till we have a complete array

Example:
[7,2,5,3,7,13,1,6] - Split the array in two sub arrays
[7,2,5,3] [7,13,1,6] - Sort the sub arrays recursively
[2,3,5,7] [1,6,7,13] - Merge the two sub arrays into one complete array

[1,2,3,5,6,7,7,13] - ARRAY IS SORTED this can be returned


The running time for the Algorithm is O(n*log(n))

'''


def MergeSort(A):
    n = len(A)
    # Check the length of array first
    if n == 1:
        return A
    # find the middle value
    m = int(n/2)
    # Split the array in two sub-arrays and solve them recursively
    B = MergeSort(A[:m+1])
    C = MergeSort(A[m+1:])
    
    # After having sorted B and C we can MERGE them
    A_Sorted = []

    
    i = j = k = 0
    # while loop to compare values between the two list
    while i < len(B) and j < len(C):
        if B[i] < C[j]:
            A_Sorted[k] = B[i]
            i += 1
        else:
            A_Sorted[k] = C[j]
            j += 1
        
        k += 1

    # moving any remaining element from the sub array to final array
    while i < len(B):
        A_Sorted[k] = B[i]
        i += 1
        k += 1

    while j < len(C):
        A_Sorted[k] = B[j]
        j += 1
        k += 1

    return A_Sorted




# Quick Sort

'''
It is a comparison based ALgorithm
running time si O(n log N) on average (beacuse the ALgo is randomized)
Note this si efficient in practice

'''

def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
  
    for j in range(low, high):
  
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
  
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
  
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
  
# Function to do Quick sort
  
  
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
  
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
  
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
  
  
# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
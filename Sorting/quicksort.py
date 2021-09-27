
def partition(arr, low, high):

    pivot = arr[high]
    i = low -1

    for j in range(low, high):
        
        if arr[j] <= pivot:

            i+=1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1


def quicksort(arr, low, high):

    if low >= high: return
    if len(arr) == 1 : return arr

    if low<high:

        index = partition(arr, low, high)

        quicksort(arr, low, index-1)
        quicksort(arr, index+1, high)


arr = [10, 7, 8, 9, 1, 5,6,55, 45,68,58,8,11,13,0,-1]
n = len(arr)
quicksort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),






    def Merge(A):

        if len(A) == 1: return A

        pivot = len(A)//2

        B = Merge(A[:pivot])
        C = Merge(A[pivot:])

        i = j = k = 0
        A_sort = []

        while i < len(B) and j < len(C):

            if B[i]< C[j]:
                A_sort.append(B[i])
                i += 1

            else:
                A_sort.append(C[i])
                j+= 1

            k += 1

        
        while i<len(B):
            A_sort.append(B[i])
            i += 1
            k += 1

        while i<len(C):
            A_sort.append(C[i])
            j += 1
            k += 1

        

            


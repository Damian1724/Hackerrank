/*
Damian Cruz
*/

#QuickSort

def quicksort(arr,low,high):
    if low < high:
        p=partition(arr,low,high)
        quicksort(arr,low,p-1)
        quicksort(arr,p+1,high)
        
def partition(arr,low,high):
    pivot=arr[low]
    border=low
    for i in range(low,high+1):
        if arr[i] < pivot:
            arr.insert(border,arr[i])
            border += 1
            arr.pop(i+1)

    return border

#InsertionSort

def insertionSort(arr):
    n=len(arr)
    for i in range(1,n):
        for j in range(i):
            if arr[i] < arr[j]:
                arr.insert(j,arr[i])
                arr.pop(i+1)

#CountingSort

def countingSort(arr):
    answer=[0]*10000
    for i in arr:
        answer[i]+=1
        
    lista=[]
    for i in range(100):
        for j in range(answer[i]):
            lista.append(i)

    return lista

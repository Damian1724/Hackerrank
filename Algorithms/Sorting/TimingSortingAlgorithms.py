/*
    Damian Cruz
*/

import time
import random

def countingSort(arr):
    answer = [0] * (max(arr)+1)
    for i in arr:
        answer[i] += 1

    lista = []
    for i in range(100):
        for j in range(answer[i]):
            lista.append(i)


def insertionSort(n, arr):
    for i in range(1,n):
        for j in range(i):
            if arr[i] < arr[j]:
                arr.insert(j,arr[i])
                arr.pop(i+1)



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

arr=[]
n=10
for i in range(3):
    for j in range(n):
        arr.append(random.randrange(1,1000000000,2))

    print("For an array on lenght",n)
    start=time.time()
    quicksort(arr,0,len(arr)-1)
    end=time.time()
    print("Time of execution for the QuickSort is",end-start,"seconds")
    start=time.time()
    insertionSort(len(arr),arr)
    end=time.time()
    print("Time of execution for the InsertionSort is",end-start,"seconds")
    start=time.time()
    countingSort(arr)
    end=time.time()
    print("Time of execution for the CountingSort is",end-start,"seconds\n")
    n*=10

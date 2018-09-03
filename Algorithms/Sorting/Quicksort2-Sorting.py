/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms>Sorting>Quicksort 2 - Sorting
problem url: https://www.hackerrank.com/challenges/quicksort2/problem
*/

def quicksort(arr,low,high):
    if low < high:
        p=partition(arr,low,high)
        quicksort(arr,low,p-1)
        quicksort(arr,p+1,high)
        print(*arr[low:high + 1])

def partition(arr,low,high):
    pivot=arr[low]
    border=low
    for i in range(low,high+1):
        if arr[i] < pivot:
            arr.insert(border,arr[i])
            border += 1
            arr.pop(i+1)

    return border

n=int(input())
arr=list(map(int,input().strip().split()))
quicksort(arr,0,len(arr)-1)

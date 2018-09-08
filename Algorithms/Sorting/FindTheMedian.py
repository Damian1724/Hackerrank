/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms>Sorting>FindTheMedian
problem url: https://www.hackerrank.com/challenges/find-the-median/problem
Cost of Algorithm: N*Log(N)
*/

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findMedian function below.
def quicksort(arr,low,high,pos):
    p = partition(arr, low, high)
    if high-p > 1 or p-low > 1:
        if pos > p:
            if min(arr[p:high]) == arr[p]:
                p+=1
            quicksort(arr,p,high,pos)
        if pos < p:
            if min(arr[low:p]) == arr[low]:
                p+=1
            quicksort(arr,low,p,pos)

def partition(arr,low,high):
    pivot=arr[low]
    border=low
    for i in range(low,high+1):
        if arr[i] < pivot:
            arr.insert(border,arr[i])
            border += 1
            arr.pop(i+1)

    return border

def findMedian(arr):
    pos=len(arr)//2
    quicksort(arr,0,len(arr)-1,pos)
    return arr[pos]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


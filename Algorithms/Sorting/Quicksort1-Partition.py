/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms>Sorting>Quicksort1-Partition
problem url:https://www.hackerrank.com/challenges/quicksort1/problem
*/


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    final=[]
    for i in range(1,len(arr)):
        if arr[i] < arr[0]:
            final.append(arr[i])
    final.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i] > arr[0]:
            final.append(arr[i])
    return final 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms>Sorting>RunningTimeofAlgorithms
problem url: https://www.hackerrank.com/challenges/runningtime/problem
*/


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    shifts=0
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                arr.insert(j,arr[i])
                arr.pop(i+1)
                shifts+=i-j
    return shifts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


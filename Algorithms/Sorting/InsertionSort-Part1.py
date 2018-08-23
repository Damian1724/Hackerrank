/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms>Sorting>InsertionSort-Part1
problem url: https://www.hackerrank.com/challenges/insertionsort1/problem
*/

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    value=arr[n-1]
    n=n-2
    while arr[n] > value:
        arr[n+1]=arr[n]
        n=n-1
        print(*arr)
        if n == -1:
            break
    arr[n+1]=value
    print(*arr)
        
        
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms>Sorting>InsertionSort-Part2
problem url:https://www.hackerrank.com/challenges/insertionsort2/problem
*/


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1,n):
        for j in range(i):
            if arr[i] < arr[j]:
                arr.insert(j,arr[i])
                arr.pop(i+1)
        print(*arr)   

               
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)


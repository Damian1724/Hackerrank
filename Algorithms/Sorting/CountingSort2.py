/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms>Sorting>CountingSort2
problem url: https://www.hackerrank.com/challenges/countingsort2/problem
*/

#!/bin/python3

import math
import os
import random
import re
import sys

def countingSort(arr):
    answer=[0]*100
    for i in arr:
        answer[i]+=1
        
    lista=[]
    for i in range(100):
        for j in range(answer[i]):
            lista.append(i)
            
    return lista

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


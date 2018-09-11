#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    dif=1000000000
    answer=[]
    arr.sort()
    for i in range(len(arr)-1):
        if  arr[i+1]-arr[i] == dif:
            answer.append(arr[i])
            answer.append(arr[i+1])
            
        if arr[i+1]-arr[i] < dif:
            answer.clear()
            answer.append(arr[i])
            answer.append(arr[i+1])
            dif=abs(arr[i]-arr[i+1])
                
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms>Implementation>Sherlock and Squares
problem url: https://www.hackerrank.com/challenges/sherlock-and-squares/problem
cost of algorithm: N
*/


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    output=0
    n=1
    while n*n<=b:
        if n*n>=a:output+=1
        n+=1
    return output
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()


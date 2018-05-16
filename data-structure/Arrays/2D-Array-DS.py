/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>arrays>2D Array-DS
problem url: https://www.hackerrank.com/challenges/2d-array/problem
*/


arr=[0]*6
for i in range(6):
    arr[i] = [int(j) for j in input().strip().split(" ")]
output=[]
for i in range(4):
    for j in range(4):
        output.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])

print(max(output))

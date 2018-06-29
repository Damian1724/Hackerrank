/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>Queue>DowntoZeroII
problem url: https://www.hackerrank.com/challenges/down-to-zero-ii/problem
*/


arr=[1000000]*1000009
arr[0]=0
arr[1]=1
arr[2]=2
for i in range(2,1000005):
    if arr[i+1]>arr[i]+1:
        arr[i+1]=arr[i]+1
    for j in range(2,i+1,1):
        if i*j>1000000:break
        if arr[i*j]> arr[i]+1:
            arr[i*j]=arr[i]+1
cases=int(input())
for i in range(cases):
    n=int(input())
    print(arr[n])


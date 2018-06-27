/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>Queue>DowntoZeroII
problem url: https://www.hackerrank.com/challenges/down-to-zero-ii/problem
*/


cases=int(input())
for i in range(cases):
    n=int(input())
    lista=[]
    lista.append(n)
    arr=[1000000]*(n+1)
    arr[n]=0
    if n==0:print(0)
    else:
        while n>3:
            sqrt=int((n**(1/2))+1)
            if arr[n-1] > arr[n]+1:
                lista.append(n - 1)
                arr[n - 1] = arr[n] + 1
            for j in range(2,sqrt,1):
                if n%j == 0 and arr[n//j] > arr[n]+1:
                    lista.append(n//j)
                    arr[n//j]=arr[n]+1

            lista.pop(0)
            n = lista[0]

        if len(arr)>=4 and n == 3 and arr[2]!=0 and arr[2]<=arr[3]:
            n=2

        if len(arr)>=4 and n == 2 and arr[3]!=0 and arr[3]<arr[2]:
            n=3

        print(arr[n]+n)

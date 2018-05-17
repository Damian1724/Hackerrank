/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms>Warmup>SimpleArraySum
problem url: https://www.hackerrank.com/challenges/simple-array-sum/problem
*/


n=int(input())
listas=list(map(int,input().split()))

def sumarraysimple(num,arr):
    res=0
    for num in arr:
        res+=num
    print(res)

sumarraysimple(n,listas)



/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms>Implementation>Between-two-sets
problem url: https://www.hackerrank.com/challenges/between-two-sets/problem
*/

n,m=input().split()
arr=list(map(int,input().strip().split()))
arr2=list(map(int,input().strip().split()))
output=0
rango=(min(arr2)-max(arr))+2
n=max(arr)
valor=True
for i in range(rango):
    for j in range(len(arr)):
        if n%arr[j]!=0:valor=False
    for j in range(len(arr2)):
        if arr2[j]%n!=0:valor=False
    n+=1
    if valor:output+=1
    valor=True

print(output)




/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>arrays>Array manipulation
problem url: https://www.hackerrank.com/challenges/crush/problem
*/


n,m=input().split()
n,m=[int(n),int(m)]
arr=[0]*(n+1)
aux=[0]*(n+1)
output=[0]*(n+1)
x=0
y=0
for i in range(m):
    a,b,k=input().split()
    a,b,k=[int(a),int(b),int(k)]
    arr[a]+=k
    aux[b]+=k

for i in range(1,(n+1)):
    x+=arr[i]
    output[i]=x-y
    y+=aux[i]

print(max(output))




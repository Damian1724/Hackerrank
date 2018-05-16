/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>arrays>Sparse Arrays
problem url: https://www.hackerrank.com/challenges/sparse-arrays/problem
*/


n=int(input())
strings=[]
for i in range(n):
    strings.append(list(map(str,input().strip().split())))
q=int(input())
queries=[]
for i in range(q):
    queries.append(list(map(str,input().strip().split())))
for i in range(q):
    output=0
    for j in range(n):
        if queries[i]==strings[j]:output+=1
    print(output)




/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name:Algorithms>Strings>StringContruction
problem url: https://www.hackerrank.com/challenges/string-construction/problem
*/


cases=int(input())
for i in range(cases):
    s=input()
    arr=[0]*len(s)
    cost=0
    for j in range(len(s)):
        if arr[(ord(s[j])-97)]==0:
            cost+=1
        arr[(ord(s[j]) - 97)]=1
    print(cost)

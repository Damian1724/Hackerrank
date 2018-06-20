/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name:Algorithms>Strings>Gemstones
problem url: https://www.hackerrank.com/challenges/gem-stones/problem
cost of algorithm: N
*/


cases=int(input())
arr=[0]*28
answer=0
for i in range(cases):
    s=input()
    for j in range(len(s)):
        if arr[ord(s[j])-96]==i:
            arr[ord(s[j])-96]+=1

for i in range(len(arr)):
    if arr[i]>=cases:answer+=int(arr[i]/cases)

print(answer)

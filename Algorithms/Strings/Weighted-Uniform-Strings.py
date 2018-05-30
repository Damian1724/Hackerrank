/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name:Algorithms>Strings>Weighted-Uniform-Strings
problem url: https://www.hackerrank.com/challenges/weighted-uniform-string/problem
cost of algorithm: N
*/


s = input()
cases = int(input())
arr = [0]*10000009
index=0

for i in range(len(s)):
    if s[i]!=s[index]:index=i
    arr[(ord(s[i])-96)*((i-index)+1)]=(ord(s[i])-96)*((i-index)+1)

for j in range(cases):
    weight=int(input())
    if arr[weight]!=0:print("Yes")
    else:print("No")


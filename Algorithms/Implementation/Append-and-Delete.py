/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms>Implementation>Append and delete
problem url: https://www.hackerrank.com/challenges/append-and-delete/problem
cost of algorithm: N
*/


s=input()
t=input()
n=int(input())
pos=0
a=min(len(s),len(t))
for i in range(a):
    if s[i]!=t[i]:break
    pos+=1
n=n-(len(s)-pos)-(len(t)-pos)
if n==0 or n>0 and n%2==0:print("Yes")
elif n >0 and n%2!=0 and n>pos*2:print("Yes")
else:print("No")


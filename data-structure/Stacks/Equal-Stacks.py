/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>Stacks>Equal-Stacks
problem url:https://www.hackerrank.com/challenges/equal-stacks/problem
cost of algorithm:N
*/


ns=list(map(int,input().strip().split()))
c1=list(map(int,input().strip().split()))
c2=list(map(int,input().strip().split()))
c3=list(map(int,input().strip().split()))
h1=sum(c1)
h2=sum(c2)
h3=sum(c3)
i=0
j=0
k=0
while h1 != 0 and h2 != 0 and h3 != 0:
    minimun=min(h1,h2,h3)
    print(h1, h2, h3,minimun)
    if h1 != minimun:
        h1-=c1[i]
        i+=1
    if h2 != minimun:
        h2-=c2[j]
        j+=1
    if h3 !=minimun:
        h3-=c3[k]
        k+=1
    if h1==h2==h3:
        print(h1)
        break
if h1 == 0 or h2 == 0 or h3 == 0:
    print(0)

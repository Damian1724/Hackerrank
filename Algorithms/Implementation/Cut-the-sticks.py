/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms>Implementation>Cut The Sticks
problem url: https://www.hackerrank.com/challenges/cut-the-sticks/problem
*/


n=int(input())
lista=list(map(int,input().strip().split()))
a=min(lista[:])
while len(lista) > 0:
    delete=[]
    a = min(lista[:])
    for i in range(len(lista)):
        lista[i]-=a
        if lista[i]==0:
            delete.append(i)
    print(len(lista))
    for j in list(reversed(delete)):
        del lista[j]


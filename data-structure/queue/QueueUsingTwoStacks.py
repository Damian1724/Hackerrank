/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>Queue>QueueUsingTwoStacks
problem url: https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
cost of algorithms: N
*/


cases=int(input())
lista=[]
for i in range(cases):
    inp=list(map(int,input().strip().split()))
    if inp[0] == 1:
        lista.append(inp[1])
    elif inp[0] == 2:
        del lista[0]
    else:
        print(lista[0])

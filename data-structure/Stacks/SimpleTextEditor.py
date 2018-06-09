/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>Stacks>SimpleTextEditor
pronlem url: https://www.hackerrank.com/challenges/simple-text-editor/problem
*/


q=int(input())
s=""
lista=[""]
i=0
for j in range(q):
    inp=list(map(str,input().strip().split()))
    a=int(inp[0])
    if len(inp)==2 and inp[1].isdigit():
        b=int(inp[1])
        if a==2:
            s=s[:(len(s)-b)]
            lista.append(s)
            i=len(lista)-1
        if a==3:print(s[b-1])

    if a == 1:
        s+=inp[1]
        lista.append(s)
        i=len(lista)-1
    if a == 4:
        i-=1
        s=lista[i]
        del lista[len(lista)-1]



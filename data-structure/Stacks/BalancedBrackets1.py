/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>Stacks>BalancedBracket
problem url: https://www.hackerrank.com/challenges/balanced-brackets/problem
cost of algorihtm: N
*/


cases=int(input())
for i in range(cases):
    s=input()
    lista=[]
    valor=True
    if len(s)%2==0:
        for j in s:
            if j =="(" or j=="[" or j=="{":lista.append(j)
            else:
                if len(lista)==0:
                    valor = False
                    break
                if j==")" and lista[len(lista)-1]!= "(" or j=="}" and lista[len(lista)-1]!= "{" or j=="]" and lista[len(lista)-1]!= "[":
                    valor=False
                    break
                if j==")" and lista[len(lista)-1]== "(" or j=="}" and lista[len(lista)-1]== "{" or j=="]" and lista[len(lista)-1]== "[":
                    del lista[len(lista)-1]
        if valor and len(lista)==0:print("YES")
        else:print("NO")
    else:print("NO")

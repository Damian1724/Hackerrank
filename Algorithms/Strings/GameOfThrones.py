/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name:Algorithms>Strings>GameOfThrones
problem url:https://www.hackerrank.com/challenges/game-of-thrones/problem
*/


s=input()
arr=[0]*27
lista=[]
valor=True
if len(s)>1:
    for i in range(len(s)):
        arr[ord(s[i])-97]+=1
    for j in range(27):
        if arr[j]!=0: lista.append(arr[j])
    if len(s)%2==0:
        for i in range(len(lista)):
            if lista[i]%2!=0:
                valor=False
                break
    elif max(lista)%2!=0 and min(lista)%2!=0:valor=False
if valor:print("YES")
if valor==False:print("NO")

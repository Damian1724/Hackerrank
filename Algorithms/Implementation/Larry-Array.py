/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms>Implementation>Larrys array
problem url: https://www.hackerrank.com/challenges/larrys-array/problem
*/

def ordering(lista,start,end):
    if lista[start]==min(lista[start:end]):return lista
    if lista[start+1]==min(arr[start:end]):
        a=lista[start]
        b=lista[start+1]
        lista[start]=b
        lista[start+1]=lista[end-1]
        lista[end-1]=a
        return lista
    if lista[end-1]==min(arr[start:end]):
        a=lista[start]
        b=lista[start+1]
        lista[start]=lista[end-1]
        lista[start+1]=a
        lista[end-1]=b
        return lista

def checking(lista):
    for i in range(len(lista)-1):
        if lista[i]>lista[i+1]:
            return False
    return True

cases=int(input())
for i in range(cases):
    elememts=int(input())
    arr=list(map(int,input().strip().split()))
    i=0
    j=3
    valor=True
    for xc in range(elememts*elememts):
        arr=ordering(arr,i,j)
        i+=1
        j+=1
        if j >elememts:
            i = 0
            j = 3
            valor = checking(arr)
            if valor:break



    if valor:print("YES")
    else:print("NO")

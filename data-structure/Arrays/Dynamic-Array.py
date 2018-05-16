/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>arrays>Dynamic Array
problem url: https://www.hackerrank.com/challenges/dynamic-array/problem
*/

 
nq = input().split()
n = int(nq[0])
q = int(nq[1])
lista=[]
matrix=[[]]
lastanswer=0

for i in range(q):
    lista=list(map(int, input().rstrip().split()))
    print(i)
    if lista[0]==1:
        if len(matrix)<= (lista[1]^lastanswer)%n:
            for j in range((len(matrix)-1),(lista[1]^lastanswer)%n):
                matrix.append([])

        matrix[(lista[1]^lastanswer)%n].append(lista[2])

    else:
        seq = (lista[1] ^ lastanswer) % n
        element = lista[2] % len(matrix[seq])
        lastanswer = matrix[seq][element]
        print(lastanswer)



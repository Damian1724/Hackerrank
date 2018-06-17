/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms>Implementation>ClimbingTheLeaderboard
problem url: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
*/


def fixing(lista):
    new=[lista[0]]
    for i in range(len(lista)-1):
        if lista[i]!=lista[i+1]:
            new.append(lista[i+1])
    return new

players=int(input())
scores=list(map(int,input().strip().split()))
alicegames=int(input())
alicescores=list(map(int,input().strip().split()))
scores=fixing(scores)
i=len(scores)-1
j=0
valor=False
while True:
    if alicescores[j]==scores[i]:
        print(i+1)
        j+=1
        valor=True
        if j >= len(alicescores):break
    if alicescores[j]<scores[i]:
        print(i+2)
        j+=1
        valor=True
        if j >= len(alicescores): break
    if alicescores[j]>=scores[0]:
        print(1)
        j+=1
        valor=True
        if j >= len(alicescores): break

    if valor==False:i-=1

    valor=False




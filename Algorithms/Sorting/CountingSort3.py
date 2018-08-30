/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms>Sorting>CountingSort3
problem url: https://www.hackerrank.com/challenges/countingsort3/problem
*/


n = int(input())
lista = []
for i in range(n):
    x, s = input().split()
    lista.append(int(x))

answer = 0
for i in range(100):
    for j in lista:
        if i == j:
            answer += 1

    print(answer)

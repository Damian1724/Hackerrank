/*
uthor: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>arrays>Left Rotation
problem url: https://www.hackerrank.com/challenges/array-left-rotation/problem
*/


a,b=input().split()
a,b=[int(a),int(b)]
lista=list(map(int,input().strip().split()))
output=[0]*a
for i in range(len(lista)):
    if i-b<0:output[len(lista)-abs(i-b)]=lista[i]
    else:
        output[i-b]=lista[i]
answer=""
for i in range(len(output)-1):
    answer+=str(output[i])+" "
answer+=str(output[len(output)-1])
print(answer)


/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>Stacks>Waiter
problem url: https://www.hackerrank.com/challenges/waiter/problem
*/


def finding_primes():
    lista=[True]*10000
    primes=[]
    for i in range(2,10000):
        if lista[i]:
            primes.append(i)
            for j in range(i+i,10000,i):
                lista[j]=False

    return primes

primes=finding_primes()
n,q=input().split()
n,q=[int(n),int(q)]
numbers=list(map(int,input().strip().split()))
output=[]
aux=[]
for i in range(q):
    del aux[:]
    for j in range((len(numbers)-1),-1,-1):
        if numbers[j]%primes[i]==0:
            output.append(numbers[j])
        else:
            aux.append(numbers[j])
    for k in range((len(output)-1),-1,-1):
        print(output[k])

    del output[:]
    del numbers[:]
    for l in aux:
        numbers.append(l)

if len(aux)>0:
    for i in range((len(aux)-1),-1,-1):
        print(aux[i])




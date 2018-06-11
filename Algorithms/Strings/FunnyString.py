/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name:Algorithms>Strings>FunnyStrings
problem url: https://www.hackerrank.com/challenges/funny-string/problem
*/


cases=int(input())
for i in range(cases):
    s=input()
    srev=''.join(reversed(s))
    i=0
    valor=True
    while i < len(s)-1:

        if (abs(ord(s[i])-ord(s[i+1])) != (abs(ord(srev[i])-ord(srev[i+1])))):
            valor=False
            break
        i+=1

    if valor:print("Funny")
    else:print("Not Funny")


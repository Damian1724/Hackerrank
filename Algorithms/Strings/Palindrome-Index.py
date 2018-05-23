/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name:Algorithms>Strings>Palindrome-Index
problem url: https://www.hackerrank.com/challenges/palindrome-index/problem
*/


def checking(word,pos):
    a=0
    b=len(word)-1
    while a<b:
        if a==pos:a+=1
        if b==pos:b-=1

        if word[a]!=word[b]:
            return  False
        a+=1
        b-=1

    return True


cases=int(input())
for i in range(cases):
    s=input()
    j=0
    k=len(s)-1
    answer=0
    valor=False
    while j < k:

        if s[j]!=s[k] and s[j+1]==s[k]:
            valor=checking(s,j)
            if valor:
                answer=j
                break
        if s[j]!=s[k] and s[j]==s[k-1]:
            valor=checking(s,k)
            if valor:
                answer=k
                break
        j+=1
        k-=1

    if valor:print(answer)
    else:print(-1)




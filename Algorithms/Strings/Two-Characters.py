/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name:Algorithms>Strings>Two Characters
problem url :https://www.hackerrank.com/challenges/two-characters/problem
*/

def eliminating(word,n1,n2,lista,answer):

    for i in range(len(lista)):
        if lista[i]!=n1 and lista[i]!=n2:
            word=word.replace(chr(lista[i]),"")
    valor=checking(word)
    if valor and len(word)>len(answer):answer=word
    return answer


def checking(word):
    for i in range(len(word)-1):
        if word[i]==word[i+1]:return False
    return True



p=int(input())
s=input()
lista=[]
arr=[0]*200
answer="0"
if len(s)>1:
    for i in range(len(s)):
        if arr[ord(s[i])]==0:
            lista.append(ord(s[i]))
            arr[ord(s[i])]=1
    for i in range(len(lista)):
        for j in range((i+1),len(lista)):
                answer=eliminating(s,lista[i],lista[j],lista,answer)

if answer!="0":print(len(answer))
else:print(0)

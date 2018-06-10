/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>Stacks>BalancedBracket
problem url: https://www.hackerrank.com/challenges/balanced-brackets/problem
cost of algorihtm: N
*/


cases=int(input())
for i in range(cases):
    s=input()
    if len(s) % 2 == 0:
        parenthesis=[0]*3
        braket=[0]*3
        braces=[0]*3
        for j in range(len(s)):
            if s[j]=="(":
                parenthesis[0]+=1
                if (j+1)%2==0:parenthesis[2]+=1
                else:parenthesis[1]+=1
            if s[j]==")":
                parenthesis[0]-=1
                if parenthesis[0]<0:break
                if (j+1)%2==0:parenthesis[2]+=1
                if (j+1)%2!=0:parenthesis[1]+=1
            if s[j]=="[":
                braket[0]+=1
                if (j+1)%2==0:braket[2]+=1
                else:braket[1]+=1
            if s[j]=="]":
                braket[0]-=1
                if braket[0]<0:break
                if (j+1)%2==0:braket[2]+=1
                if (j+1)%2!=0:braket[1]+=1
            if s[j]=="{":
                braces[0]+=1
                if (j+1)%2==0:braces[2]+=1
                else:braces[1]+=1
            if s[j]=="}":
                braces[0]-=1
                if braces[0]<0:break
                if (j+1)%2==0:braces[2]+=1
                if (j+1)%2!=0:braces[1]+=1
        if parenthesis[0]==0 and braket[0]==0 and braces[0]==0 and parenthesis[1]==parenthesis[2] and braces[1]==braces[2] and braket[1]==braket[2]:
            print("YES")
        else:print("NO")
    else:print("NO")





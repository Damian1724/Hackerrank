/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name:Algorithms>Strings>Mars Exploration
problem url: https://www.hackerrank.com/challenges/mars-exploration/problem
*/


s=input()
c="SOS"*int((len(s)/3))
answer=0
for i in range(len(s)):
    if s[i]!=c[i]:answer+=1
print(answer)

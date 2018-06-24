/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms>Warmup>TimeConversion
problem url:https://www.hackerrank.com/challenges/time-conversion/problem
*/


s=input()
if s[8]=="A":
    s=s.replace("AM","")
    s = s.split(":")
    if s[0]=='12':
        s[0]="00"
    print(":".join(s))
else:
    s = s.replace("PM", "")
    s = s.split(":")
    if s[0]!="12":
        s[0]=str(int(s[0])+12)
    print(":".join(s))








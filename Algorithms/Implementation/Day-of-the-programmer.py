/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms>Implementation>Day of the programmer
problem url: https://www.hackerrank.com/challenges/day-of-the-programmer/problem
*/


n=int(input())
if n==1918:
    print("26.09.1918")
else:
    if n>=1700 and n<=1917:
        if n%4==0:
             print("12.09."+str(n))
        else:
            print("13.09."+str(n))
    else:
        if n%400==0 or n%4==0 and n%100!=0:
            print("12.09." + str(n))
        else:
            print("13.09." + str(n))

/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms>Implementation>Strange Counter
problem url: https://www.hackerrank.com/challenges/strange-code/problem
cost of algorithm: N
*/


input=int(input())
value=3
time=1
while value+time<=input:
    time+=value
    value*=2
print(value-(input-time))

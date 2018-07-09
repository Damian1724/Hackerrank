/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>Tress>Tree: Huffman Decoding
problem url: https://www.hackerrank.com/challenges/tree-huffman-decoding/problem
*/


"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    current=root
    for i in s:
        if i == "1":
            current=current.right
        if i =="0":
            current=current.left
        if current.left is None and current.right is None:
            print(current.data,end="")
            current=root

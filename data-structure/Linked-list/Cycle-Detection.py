/*
uthor: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>linked lists >Cicle Detection
problem url: https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem
cost of algorithm: N
*/


"""
 Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if head !=None:
        i=0
        while head.next is not None:
            i+=1
            head=head.next
            if i>=101:return True
    return False

/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>linked lists >Delete-duplicate-value-nodes-from-a-sorted-linked-list
problem url: https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem
"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
    pointer=headB
    while headA.next is not None:
        while headB.next is not None:
            if headA.next==headB.next:
                return headA.next.data
            headB=headB.next
        headB=pointer
        headA=headA.next
    
       
            

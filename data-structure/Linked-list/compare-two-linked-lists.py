/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>linked lists > Compare two linked lists
problem url:https://www.hackerrank.com/challenges/compare-two-linked-lists/problem
*/    
"""
 Merge two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
def CompareLists(headA, headB):
    while headA.data == headB.data and headA.next is not None and headB.next is not None:
        headA=headA.next
        headB=headB.next
    
    if headA.data == headB.data and headA.next == headB.next:return 1
    else:return 0

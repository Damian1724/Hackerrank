/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>linked lists >Insert-a-Node-at-the-Tail-of-a-Linked-List
problem url: https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem
*/


"""
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 return back the head of the linked list in the below method
"""

def Insert(head, data):
    pointer=head
    aux_node=Node(data)
    if head==None:return aux_node
    else:
        while head.next is not None:
            head=head.next
        head.next=aux_node
        return pointer

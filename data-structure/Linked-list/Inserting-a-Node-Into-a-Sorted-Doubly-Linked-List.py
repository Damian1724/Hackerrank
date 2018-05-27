/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>linked lists > Inserting a Node Into a Sorted Doubly Linked List
problem url: https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem
cost of the algorithm: N
 */ 
 
 
"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def SortedInsert(head, data):
    if head.data < data:
        insert=Node(data)
        pointer=head
        while head.next is not None and head.next.data < insert.data:
            head=head.next
        aux=head.next
        head.next=insert
        head.next.prev=head.data
        head.next.next=aux
        return pointer
    else:
        aux=head
        insert=Node(data)
        head=insert
        head.next=aux
        head.next.prev=head.data
        return head
        

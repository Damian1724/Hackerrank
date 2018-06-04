/*
author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>linked lists >Reverse a doubly linked list
problem url: https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem
cost of the algorithm: N
*/


"""
 Reverse a doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def reverse(head):
    if head.next is None:return head
    aux=head.next
    aux2=head.prev
    head.prev=aux
    head.next=aux2
    n=head
    while head.prev is not None:
        head=head.prev
        aux=head.next
        aux2=n
        head.prev=aux
        head.next=aux2
        n=head
    return head   

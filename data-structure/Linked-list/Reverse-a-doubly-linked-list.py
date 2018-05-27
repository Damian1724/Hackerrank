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
def Reverse(head):
    if head.next is None:return head
    output = Node(head.data)
    while head.next is not None:
        head = head.next
        aux=output
        adding=Node(head.data)
        output=adding
        output.next=aux
        output.next.prev=adding
    return output

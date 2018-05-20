/*
author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>linked lists >https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem
problem url: https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem
*/


"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.

def InsertNth(head, data, position):
    aux=Node(data)
    if position ==0 or head==None:
        aux.next=head
        return aux
    
    if position !=0:
        i=1
        first=head
        while i < position and head.next is not None:
            i+=1
            head=head.next
        if head.next is None:
            head.next=aux
        else:
            aux.next=head.next
            head.next=aux
            
        return first
            

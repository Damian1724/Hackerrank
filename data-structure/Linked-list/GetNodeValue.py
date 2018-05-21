/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>linked lists >Get Node Value
problem url: https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem
*/


#Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""
def get_lenght(aux):
    lenght=0
    while aux.next is not None:
        lenght+=1
        aux=aux.next
    return lenght
        
def GetNode(head, position):
    aux=head
    lenght=get_lenght(aux)
    lenght=lenght-position
    j=0
    while j <= lenght:
        if j==lenght:return head.data
        head=head.next
        j+=1
        

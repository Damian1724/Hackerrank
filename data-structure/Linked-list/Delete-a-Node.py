/*
author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>linked lists >Delete a Node
problem url: https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem
*/


"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    aux=head
    if position==0:
        head=head.next
        return head
    
    else:
        i=1
        while i < position and  head.next is not None:
            i+=1
            head=head.next
        if head.next.next is None:
            head.next=None
        else:
            head.next=head.next.next
    
        return aux
        
    
        
    

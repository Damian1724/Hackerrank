*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>linked lists > Delete duplicate-value nodes from a sorted linked list
problem url: https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem
*/


"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def jumping(head):
    aux = head
    while aux.next is not None and head.data == aux.next.data:
        aux=aux.next
    return aux

def RemoveDuplicates(head):
    pointer=head
    if head == None:
        return head
    else:
        while head.next is not None:
            if head.data == head.next.data:
                aux=jumping(head)
                if aux.next is None:
                    head.next=None
                    break
                else:
                    aux=aux.next
                    head.next=aux
            head=head.next

        return pointer

            
            
            
            
            

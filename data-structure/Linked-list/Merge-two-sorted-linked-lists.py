/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>linked lists > Merge two sorted linked lists
problem url: https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem
*/


"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
def adding_remaining_elements(output,head):
        while output.next is not None and output.next.data < head.data:
                output=output.next
        aux=output.next
        output.next=head
        output.next.next=aux
        
def MergeLists(headA,headB):
    if headA==None:return headB
    if headB==None:return headA
    
    output=Node()
    
    if headA.data < headB.data:
        output=headA
        headA=headA.next
    else:
        output=headB
        headB=headB.next
        
    pointer=output
    while headA.next is not None and headB.next is not None:
        if headA.data > headB.data:
            output.next=headB
            output=output.next
            headB=headB.next
            output.next=headA
        else:
            output.next=headA
            output=output.next
            headA=headA.next
            output.next=headB
            
    if headA != None and headA.next is None:
        adding_remaining_elements(output,headA)
    if headB != None and headB.next is None:
        adding_remaining_elements(output,headB)
        
    return pointer
    
    
    
    
    
    
    
    
    
    
    

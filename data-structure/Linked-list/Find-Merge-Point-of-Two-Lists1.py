/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>linked lists > Find Merge Point of Two Lists
problem url: https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem
cost of algorithm:N
*/


"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""
def inversing(head,link_list):
    while head.next is not None:
        head=head.next
        add_node=link_list
        aux=Node(head.data)
        link_list=aux
        link_list.next=add_node
    return link_list
def FindMergeNode(headA, headB):
    rev_a=Node(headA.data)
    rev_b=Node(headB.data)
    rev_a=inversing(headA,rev_a)
    rev_b=inversing(headB,rev_b)
    while rev_a.next.data == rev_b.next.data:
        rev_a=rev_a.next
        rev_b=rev_b.next
    return rev_a.data

   
    
    
       
            

/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>linked lists >Print in reversed
problem url: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem
cost of algorithm: N
*/


"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def reversePrint(head):
    if head is not None:
        output=SinglyLinkedListNode(head.data)
        while head.next is not None:
            head=head.next
            aux=output
            add_node=SinglyLinkedListNode(head.data)
            output=add_node
            output.next=aux
        while output.next is not None:
            print(output.data)
            output=output.next
        print(output.data)

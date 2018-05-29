/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>linked lists >PrintLinkedlist
problem url: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem
cost of algorithm: N
*/


# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):
    if head is not None:
        print(head.data)
        while head.next is not None:
            head=head.next
            print(head.data)
        

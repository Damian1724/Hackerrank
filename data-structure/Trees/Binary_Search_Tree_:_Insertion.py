/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>Tress>Binary Search Tree : Insertion
problem url: https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem
*/


#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        if self.root is None:
            self.root=Node(val)
        else:
            current = self.root
            while True:
                if val < current.info:
                    if current.left is None:
                        current.left=Node(val)
                        break
                    else:
                        current=current.left
                else:
                    if current.right is None:
                        current.right=Node(val)
                        break
                    else:
                        current=current.right

/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>Tress>Tree:top_view
problem url:https://www.hackerrank.com/challenges/tree-top-view/problem
*/


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    arr = [0] * 505
    left = 0
    right = 0
    lista=[]
    output=[]
    if root is not None:
        lista.append(root)
        output.append(root.info)
        output=going_over_tree( arr, left, right,lista,output)
        for i in output:
            print(i,end=" ")
    
def going_over_tree(arr,left,right,lista,output):
        while len(lista) > 0:
            if lista[0].left is not None:
                lista.append(lista[0].left)
                arr[lista[0].left.info] = arr[lista[0].info] - 1
                if arr[lista[0].left.info] < left:
                    left = arr[lista[0].left.info]
                    output.insert(0,lista[0].left.info)
                    
            if lista[0].right is not None:
                lista.append(lista[0].right)
                arr[lista[0].right.info] = arr[lista[0].info] + 1
                if arr[lista[0].right.info] > right:
                    right = arr[lista[0].right.info]
                    output.append(lista[0].right.info)
            lista.pop(0)
        return output

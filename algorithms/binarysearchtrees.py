from dataclasses import dataclass
from typing import Any

@dataclass
class TreeNode:
    
    value: Any = None
    leftchild: Any = None
    rightchild: Any = None
    
    
    
def search(searchvalue, node):
    
    # base case: if the node is nonexistent or we've fount the target value
    if node is None or node.value == searchvalue:
        return node
    
    # perform search on left subtree if value is less than current node value
    elif searchvalue < node.value:
        return search(searchvalue, node.leftchild)
    
    # perform search on right subtree if value is less than current node value
    elif searchvalue > node.value:
        return search(searchvalue, node.rightchild)
    
def insert(value, node):
    
    if value < node.value:
        
        # if the left child does not exist, we want to insert
        # the value as the left child
        if node.leftchild is None:
            node.leftchild = TreeNode(value)
        else:
            insert(value, node.leftchild)
    
    elif value > node.value:
        
        # if the right child does not exist, we want to insert
        # the value as the right child
        if node.rightchild is None:
            node.rightchild = TreeNode(value)
        else:
            insert(value, node.rightchild)
    
def delete(valueToDelete, node):
    
    # base case: we've hit the bottom of the tree and the parent node has no children
    if node is None:
        return None
        
    
    # if target value is less or greater than the current node, 
    # we set the left or right child respectively to be
    # the return value of a recursive call of this 
    # very method of the current node's left or right subtree
    elif valueToDelete < node.value:
        node.leftchild = delete(valueToDelete, node.leftchild)
        
        # return the node (and its subtree if existent) to
        # be used as a new value of its parent's left or right child
        return node
    
    elif valueToDelete > node.value:
        node.rightwhild = delete(valueToDelete, node.rightchild)
        
    # if current node is the one we want to delete
    elif valueToDelete == node.value:
        
        # if the current node has no left child, we delete it by
        # returning its right child (and subtree if existent)
        # to be its parent's subtree
        if node.leftchild is None:
            return node.rightchild
        
        elif node.rightchild is None:
            return node.leftchild
        
        
        # if the current node has two children, delete the current node
        # by calling the lift function (below),
        # which changes the current node's
        # value to the value of its successor node
        else:
            node.rightchild = lift(node.rightchild, node)
            return node

def lift(node, nodeToDelete):
    
    # if current node has a left child,
    # recursively call this func to continue down
    # left subtree to find successor node
    if node.leftchild:
        node.leftchild = lift(node.leftchild, nodeToDelete)
        
    # if the current node has no left child, that means current node
    # of this func is the successor node, and we take its value
    # and make it the new value of the node we're deleting
    else:
        nodeToDelete.value - node.value
        
        return node.rightchild
    
    
def traverse_print(node):
    if node is None:
        return
    
    traverse_print(node.leftchild)
    print(node.value)
    traverse_print(node.rightchild)
    

def findmax(node):
    """The greatest value will always be the rightmost leaf,
       so this func recursively goes accesses each right node
       and returns the value of the rightmost node"""
       
    if node.rightchild:
        return findmax(node.rightchild)
    else:
        return node.value

    
        
    
    
    
    
n1 = TreeNode(10)

for i in [13, 5,3,6,1,4]:
    insert(i,n1)
    

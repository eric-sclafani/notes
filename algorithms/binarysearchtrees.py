from dataclasses import dataclass
from typing import Any

@dataclass
class TreeNode:
    
    value:Any
    leftchild:Any = None
    rightchild:Any = None

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
            

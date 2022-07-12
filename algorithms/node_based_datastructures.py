from dataclasses import dataclass
from typing import Any

#
##
### CODE FOR SINGLY LINKED LISTS
##
#


@dataclass
class Node:
    data:Any
    next_node:None = None
    
@dataclass   
class LinkedList:
    """When using a linked list, we only have immediate access to the first node"""
    first_node:Node
    
    def printnodes(self):
        
        node = self.first_node
        index = 0
        while node:
            print(f"Node {index}: {node.data}")
            index += 1
            node = node.next_node
        
    
    def read(self, index):
        
        current_node = self.first_node
        current_index = 0
        
        while current_index < index:
            
            current_node = current_node.next_node
            current_index += 1
            if not current_node:
                return None
        return current_node.data
    
    def index_of(self, value):
        current_node = self.first_node
        current_index = 0
        
        while True:
            if current_node.data == value:
                return current_index
            else:
                current_node = current_node.next_node
                current_index += 1
                
                if not current_node:
                    return None
                
    def insert_at_index(self, index, value):
        """Opposite time complexity as array insertion: 
        
        - Beginning of linked list = O(1)
        - End of linked list = O(N)
        vs.
        - Beginning of array = O(N)
        - End of array = O(1)
        """
        
        new_node = Node(value)
        
        if index == 0: # if inserting at beginning of linked list
            
            # have out new node link to what was previousley the first node
            new_node.next_node = self.first_node
            
            # re-assign self.first_note to our new node
            self.first_node = new_node
            
        else: # if we're inserting anywhere else besides the beginning
            
            current_node = self.first_node
            current_index = 0
            
            # first, we access the node immediately before
            # where the new node will go
            while current_index < (index-1):
                current_node = current_node.next_node
                current_index += 1
                
            # have the new node link to the next node
            new_node.next_node = current_node.next_node
            
            # modify the link of the previous node to point to the new node
            current_node.next_node = new_node
            
    def delete_at_index(self, index):
        """With linked lists, deleting a node simply means removing 
           the pointer pointing to the node you want to delete and reassigning 
           the previous node to point to the next node after the one you want deleted """
        
        if index == 0:
            self.first_node = self.first_node.next_node
            
        else:
            
            current_node = self.first_node
            current_index = 0
            
            while current_index < (index-1):
                current_node = current_node.next_node
                current_index += 1
                
            # find the node that comes after the one we're deleting
            node_after_deleted_node = current_node.next_node.next_node
            
            # change the link of current_node to 
            # point to the node_after_deleted_node, leaving
            # the node we want to delete out of the list
            current_node.next_node = node_after_deleted_node
    
    def get_last_element(self):
        
        current_node = self.first_node
        
        if not current_node.next_node: # one item in list
            return current_node.data
        else:
            while True:
                current_node = current_node.next_node
                if not current_node.next_node:
                    break
                
        return current_node.data
    
    def reverse_list(self):
        
        current_node = self.first_node
        previous_node = None
        
        while current_node:
            
            next_node = current_node.next_node
            current_node.next_node = previous_node
            
            previous_node = current_node
            current_node = next_node
        
        self.first_node = previous_node
        
        
    def delete_mid_node(self, node):
        node.data = node.next_node.data
        node.next_node = node.next_node.next_node
            

        
        
        
node1 = Node("Hello")
node2 = Node(2)
node3 = Node(3)
node1.next_node = node2
node2.next_node = node3    
         
mylist = LinkedList(node1)
mylist.reverse_list()

            
            
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
            
#
##
### CODE FOR DOUBLY LINKED LISTS
##
#           
   
@dataclass         
class Node:
    
    data:Any
    next_node:None = None
    previous_node:None = None

@dataclass
class DoublyLinkedList:
    
    first_node:Node = None
    last_node:Node = None
    
    def reverseprint(self):
        
        node = self.last_node
        while node:
            
            print(f"Node: {node.data}")
            node = node.previous_node
    
    def insert_at_end(self, value):
        """
        Since a doubly linked list always knows where the first and last nodes are, 
        we can access them in a single step
        """
        new_node = Node(value)
        
        if not self.first_node: # if there are no elements yet in the linked list
            self.first_node = new_node
            self.last_node = new_node
            
        else: # if the linked list already has at least 1 node
            
            # set previous_node link of our new node to point to the previous last_node,
            # effectively placing the new node at the end of the linked list
            new_node.previous_node = self.last_node
            
            # change the previous last_node's link to point to our new_node
            self.last_node.next_node = new_node
            
            # lastly, we tell this instance of DoublyLinkedList that it's new last_node is our new_node
            self.last_node = new_node
            
    def remove_from_front(self):
        
        removed_node = self.first_node # store the current first node
        self.first_node = self.first_node.next_node # re-assign the first node to be the next_node, effectively removing the previous first node
        return removed_node
    
@dataclass
class Queue:
    
    data:DoublyLinkedList = DoublyLinkedList()

    def enqueue(self, element):
        self.data.insert_at_end(element)
        
    def dequeue(self):
        removed_node = self.data.remove_from_front()
        return removed_node.data
    
    def read(self):
        
        if not self.data.first_node:
            return None
        else:
            return self.data.first_node.data
  
  
node0 = Node("Hello")
node1 = Node("my")
node2 = Node("name")
node3 = Node("is")
node4 = Node("Eric")

node0.next_node = node1
node1.next_node = node2  
node2.next_node = node3  
node3.next_node = node4  

node1.previous_node = node0
node2.previous_node = node1
node3.previous_node = node2 
node4.previous_node = node3        
     
   
dlist = DoublyLinkedList(node0,node4)

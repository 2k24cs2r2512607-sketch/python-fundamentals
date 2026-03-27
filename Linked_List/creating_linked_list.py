# Simple implementation of a singly linked list in Python
class Node:
    def __init__(self, data):
        self.data = data  # The value stored in the node
        self.next = None  # Pointer to the next node  
 
head=Node(5)       # First node (head of the linked list)
second=Node(10)     
head.next =second   # Link first node to second node
print("Data in the second node:", head.next.data)
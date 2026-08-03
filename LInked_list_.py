class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__ (self,data):
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node
        self.length += 1
        

        
n1 = Node(10)
print(n1.data)

        
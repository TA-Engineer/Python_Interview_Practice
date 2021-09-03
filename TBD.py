class Node:
    def __init__ (self, val = None, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__ (self):
        self.head = None
        self.tail = self.head

    # Function to append to the linked List at the End

    def pushBack(self, data, method = 'head'):
        new_node = Node(data)
        if method == 'head':
            current_node = self.head
            while current_node != None:
                current_node = current_node.next
            
            current_node.next = new_node
            self.tail = new_node
        
        elif method == 'tail':
            self.tail.next = new_node
            self.tail = new_node

        else:
            raise NameError("Incorrect option defined for 'Method' argument")


    
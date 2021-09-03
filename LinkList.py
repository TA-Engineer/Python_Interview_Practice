# This is a file for working with the basic of a LinkedList

# SINGLE LINKED LIST

class Node:
    def __init__(self, val=None, next = None):
        
        self.val = val
        self.next = next

class Linked_list:
    def __init__(self):
        self.head = Node()
        self.tail = None

    # Now creating the append function or PushBack
    '''
    Steps:
    1. To add the new data point in the back of the linkedlist we will first convert it into a node
    2. then we will create a current node to look at the head pointer (which is basically pointing to a val and next)
    3. Then we will loop to the end of te list using a while loop
    4. Once at the end we will point the end node of the linkedList to the new node
        This will add the object to the back

    NOTE: while working with the head operation tail will also be updated to the end of the linked list
    '''
    def pushBack(self,data, method = 'head'):
        if self.head.next == None:
            self.pushFront(data)
        else:  
            new_node = Node(data)
            if method == 'head':
                current_node = self.head
                
                while (current_node.next != None):
                    current_node = current_node.next
                
                current_node.next = new_node
                self.tail = new_node
            
            elif method == 'tail':
                self.tail.next = new_node
                self.tail = new_node

            else:
                raise NameError("Incorrect option defined for 'Method' argument")
        
        # print("Push Back - head value: ",self.head.next.val)
        # print("Push Back - Tail value: ",self.tail.val)


    def pushFront(self, data):
        new_node = Node(data)
        # if self.head.next != None:
            # print("Before PushFront - head value:", self.head.next.val)
        current_node = self.head.next
        new_node.next = current_node
        self.head.next = new_node
        
        if self.tail == None:
            self.tail = self.head.next
            # print(self.tail)
        
        
        # if self.head.next != None:
        #     print("PushFront - head value:", self.head.next.val)
        # print("-PushFront - tail value: ",self.tail.val)



    # Function to find the length of the linked list
    def length(self):
        current_node = self.head
        total = 0
        while current_node.next != None:
            total += 1
            current_node = current_node.next
        return total

    # Function to display the current content of our list
    def display(self):
        elements = []
        current_node = self.head
        
        
        while current_node.next != None:
            # break
            current_node = current_node.next
            elements.append(current_node.val)

        print("Display - Head value: ",self.head.next.val)
        print("Display - Tail value: ",self.tail.val)
        

        print(elements)

    def get(self, index):
        if index >= self.length():
            print("ERROR: Get index is out of range")
            return
        current_idx = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_idx == index: return current_node.val
            current_idx += 1
    
    def popFront(self):
        if self.head.next == None:
            raise RuntimeError("The List is Empty")

        else:
            self.head.next = self.head.next.next
            # if self.head.val == None:
            #     self.tail = None
            # else:
            #     tail.next


    # Function to erase a value from the linked List
    def erase(self, index):
        if index >= self.length():
            print(" Error: Erase index is out of range")
            return
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1

    # Function to insert value after an index
    def insertAfter(self, data, index):
        new_node = Node(data)
        if index >= self.length():
            raise RuntimeError("Index value if greater than length of the list")
            return

        if index == -1:
            self.pushFront(data)
            return
        elif index == self.length()-1:
            self.pushBack(data)
            return 
        
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if index == current_index:
                last_node = current_node
                current_node = current_node.next
                last_node.next = new_node
                new_node.next = current_node   
                return
            
            current_index += 1




        


    



# Now looking at the values of the list

my_list = Linked_list()
# my_list.display()
my_list.pushFront(10)
my_list.pushBack(1)
my_list.pushBack(2,"tail")
my_list.pushBack(3)
my_list.pushBack(4, 'tail')
my_list.popFront()
# my_list.display()
my_list.pushFront(9)

# my_list.display()

# print(" Element in the 2nd index is: ", my_list.get(2))

# my_list.erase(1)
my_list.insertAfter(5,4)

my_list.display()
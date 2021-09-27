# https://www.youtube.com/watch?v=f5dU3xoE6ms&t=1479s


class Node:
    def __init__ (self, value = None):
        # The useer will not interact with this class. This is just a wrapper for the binary serarch tree class

        self.value = value
        self.left_child = None
        self.right_child = None
     

class BinarySearchTree:

    def __init__ (self):
        self.root = None # as iniitally we don't have any elements in the tree
            
    def insert(self, value):
        # Here we will check if the root has any value yet or not 
        # if there are not values in the root then we will set the root to none
        # This means that root is the value itself

        if self.root == None:
            # we will create a new node for the root node
            self.root = Node(value)

        else:
            # we will insert through a private function
            self._insert(value, self.root)

    def _insert(self, value, curr_node):
        # check if the value is less than the current node
        if  value < curr_node.value:
            # first we will check if the current node does not have a left child

            if curr_node.left_child == None:
                curr_node.left_child = Node(value)
            else:
                self._insert(value, curr_node.left_child)
        
        elif value > curr_node.value: # the value is greater than the current node value

            if curr_node.right_child == None:
                curr_node.right_child = Node(value)
            else:
                self._insert(value, curr_node.right_child)
        
        else: # this is where the value == current node value
            print("Value is already in the tree")


    def  height(self):
        if self.root != None:
            return self._height(self.root,0)
        else:
            return 0
        
    def _height(self, curr_node, curr_height):
        if curr_node == None: return curr_height
        left_height = self._height(curr_node.left_child, curr_height+1)
        right_height = self._height(curr_node.right_child, curr_height+1)
        return max(left_height,right_height)

    def print_tree(self): 
        if self.root != None:
            self._print_tree(self.root)

        
    def _print_tree(self,curr_node):
        if curr_node != None:
            self._print_tree(curr_node.left_child)
            # THis is basically inorder traversal of the tree
            print(str(curr_node.value))
            self._print_tree(curr_node.right_child)
    
    
    # creating a function to search in the tree
    def search(self, value):
        if self.root != None: 
            return self._search(value, self.root)
        else: 
            return False
    
    def _search(self, value, curr_node):
        if value == curr_node.value:
            return True
        elif value < curr_node.value and curr_node.left_child != None:
            return self._search(value, curr_node.left_child)
        elif value > curr_node.value and curr_node.right_child != None:
            return self._search(value, curr_node.right_child)

        return False




# creating a fucntion to fill the tree

def fill_tree (tree, num_elems = 100, max_int= 1000):
    from random import randint
    for _ in range(num_elems):
        curr_elems = randint(0,max_int)
        tree.insert(curr_elems)

    return tree





# practice code

# tree = BinarySearchTree()

# tree.insert(5)
# tree.insert(1)
# tree.insert(3)
# tree.insert(7)
# tree.insert(6)
# tree.insert(9)
# tree.insert(0)
# tree.insert(19)
# tree.insert(31)
# tree.insert(13)

# # tree = fill_tree(tree)

# tree.print_tree()

# print("Tree height is: ", str(tree.height()))


# print(tree.search(31))
# print(tree.search(2))
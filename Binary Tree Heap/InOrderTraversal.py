class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None


class Binary_Tree:

    def __init__(self):
        self.root = None

    def Insert(self, value):
        if self.root == None:
            self.root = Node(value)

        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):

        if value < current_node.value:
            if current_node.leftChild == None:
                current_node.leftChild = Node(value)

            else:
                self._insert(value, current_node.leftChild)

        elif value > current_node.value:
            if current_node.rightChild == None:
                current_node.rightChild = Node(value)

            else:
                self._insert(value, current_node.rightChild)

        else: 
            print("Value is already in the tree")


    def size(self, curr_node = self.root):
        if curr_node == None:
            return 0
        else:
            return 1 + self.size(curr_node.leftChild) + self.size(curr_node.rightChild)

    def height(self, curr_node = self.root):
        if curr_node == None:
            return 0
        return 1 + max(self.height(curr_node.leftChild), self.height(curr_node.rightChild))



    # def print_tree(self):
    #     pass

    def InorderTraversal(self, curr= self.root):
        if curr == None:
            return 
        self.InorderTraversal(curr.leftChild)
        print(curr.value)
        self.InorderTraversal(curr.rightChild)


# practice code

tree = BinarySearchTree()

tree.insert(5)
tree.insert(1)
tree.insert(3)
tree.insert(7)
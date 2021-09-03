# LINKED LIST QUESTION

class ListNode:
    def __init__(self , vl=0, next_node=None):
        self.val = val
        self.next = next
# Merging two sorted Linked List

def merge_two_sorted_Linked_List(l1,l2):
    # Step 1: Create a new linked list
    new_node = ListNode()
    head_node = new_node

    while l1 and l2:
        if l1.data< l2.val:
            new_node.next = l1.val
            l1 = l1.next

        else:
            new_node.next = l2.val
            l2 = l2.next
        new_node = new_node.next

        new_node.next = l1 or l2

        return head_node.next

# Code for reversing a linked list


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode()
        previous = None
        new_node.next = head
        current_node = head
        
        while current_node!= None:
            
            print(current_node.val)
            
            next = current_node.next
            
            # Reverse
            current_node.next = previous
            previous = current_node
            # print("previous: ", previous)
            current_node = next     
            # if current_node != None:
            #     print("new curr: ", current_node.val)
                
        head = previous    
        return head

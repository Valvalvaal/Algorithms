from LinkedList import LinkedList
from Node import Node
# T: O(n), S: O(n)
def insert_at_tail(head, value):
    "Insert node with given value at the end of a linked list"
    if not head:
        return Node(value)
    
    curr = head
    
    while curr.next_element:
        curr = curr.next_element
    curr.next_element = Node(value)  

    return head

lst = LinkedList()

lst.insert_at_head(1)
lst.insert_at_head(3)
lst.insert_at_head(5)
lst.insert_at_head(6)

lst.print_list()

insert_at_tail(lst.head_node, 100)

lst.print_list()
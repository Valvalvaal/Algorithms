# Definition for a Linked List node
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ds_v1.LinkedList.LinkedList import ListNode

def remove_nth_last_node(head, n):
    
    # For my solution, I'll use two pointers to traverse the entire linked list. 
    # The pointers will be n steps away from each other. That way, when the pointer
    # that's ahead reaches the end of the array, the remaining pointer will be on the
    # node I want to remove.
    p1 = head
    p2 = head
    
    while n:
        p1 = p1.next
        n -= 1
        
    if not p1:
        return head.next
    
    while p1.next:
        p1 = p1.next
        p2 = p2.next
    
    p2.next = p2.next.next
        
    return head


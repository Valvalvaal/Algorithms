# Definition for a Linked List node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# T: O(N), S:O(1)
def remove_nth_last_node(head, n):
    
    # For my solution, I'll use two pointers to traverse the entire linked list. 
    # The pointers will be n steps away from each other. That way, when the pointer
    # that's ahead reaches the end of the array, the remaining pointer will be on the
    # node I want to remove.
    
    # define pointers at the beginning of the list
    fast = head
    slow = head
    
    # Fast will be n steps ahead of slow
    while n:
        fast = fast.next
        n -= 1
    
    # If fast is already after the last node, it means the slow pointer is already
    # standing on the slow node, so we return the next node from the original head as
    # the head node for the return list. 
    if not fast: 
        return head.next
    
    # Continue traversing the list until we get to the last node   
    while fast.next:
        fast = fast.next
        slow = slow.next
    
    # Slow pointer points at the node n+1 from the end, so we eliminate the node n 
    # steps from the end by jumping over it and pointing to the next.next node
    slow.next = slow.next.next    
        
    return head


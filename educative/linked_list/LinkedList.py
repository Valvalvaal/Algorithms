from Node import Node

class LinkedList:
    def __init__(self):
        self.head_node = None

    def delete_at_head(self):
        if self.is_empty():
            return None
        
        removed_node = self.head_node
        self.head_node = removed_node.next_element
        removed_node.next_element = None  # explicit unlinking of deleted node

        return removed_node.data

    def insert_at_head(self, data):
        # T: O(1)
        temp_node = Node(data) # create node to insert
        temp_node.next_element = self.head_node # make new node point to prev head
        self.head_node = temp_node # update the head node w/ new head
        return self.head_node

    def get_head(self):
        # T: O(1)
        return self.head_node
    
    def is_empty(self):
        # T: O(1)
        if not self.head_node:
            return True
        else:
            return False
        
    def print_list(self):
        if self.is_empty():
            print("Empty lsit")
            return False
        
        temp = self.head_node
        while temp.next_element:
            print(temp.data, "->")
            temp = temp.next_element

        print(temp.data, "-> None")
        return True

lst = LinkedList()
print(lst.is_empty())
print(lst.get_head())

lst.insert_at_head(1)
lst.insert_at_head(3)
lst.insert_at_head(5)
lst.insert_at_head(6)

lst.print_list()

print("deleted: ",lst.delete_at_head())

lst.print_list()
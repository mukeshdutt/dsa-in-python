class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def create_node(self, data):
        """creating a new node in a linked list"""
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        return
    
    def traversal_linked_list(self):

        temp = self.head
        while temp:
            print(f"{temp.data}", end=" -> ")
            temp = temp.next
        print("None")


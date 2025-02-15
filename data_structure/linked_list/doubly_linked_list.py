
class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None

class DoublyLinkedList: 
    
    def __init__(self):
        self.head = None
    
    def create_node(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        
        if self.head is not None:
            temp = self.head
            prev_node = None
            while temp:
                prev_node = temp
                temp = temp.next

            new_node = Node(data)
            new_node.prev = prev_node
            prev_node.next = new_node
            # temp = new_node

    def insert_at_end(self, data):
        temp = self.head
        prev_node = None
        while temp:
            prev_node = temp
            temp = temp.next
        
        new_node = Node(data)
        new_node.prev = prev_node
        prev_node.next = new_node
        return

    def insert_at_position(self, data, position):
        
        temp = self.head
        prev_node = None
        count = 1
        while temp:
            if count == position:
                new_node = Node(data)
                new_node.prev = prev_node
                new_node.next = temp
                prev_node.next = new_node
                return
                
            prev_node = temp
            temp = temp.next
            count += 1

    def delete_from_end(self):
        pass

    def delete_from_position(self):
        pass

    def traversal_forward(self):
        temp = self.head
        while temp:
            print(f"{temp.data}", end=" -> ")
            temp = temp.next
        print(" None")

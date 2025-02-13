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

    def insert_at_begin(self, data):
        """head node is taking into a temp node and iterating the temp node and filling data into head node"""
        temp = self.head
        self.head = Node(data)
        self.head.next = temp
        return

    def insert_at_end(self, data):
        """insert data at the end"""
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)

    def length(self):
        temp = self.head
        count = 0

        # when list is empty
        if self.head is None:
            return 0

        # when list has data available
        if self.head is not None:
            count = 1
            while temp:
                count += 1
                temp = temp.next
                return count

    def insert_at_postion(self, pos, data):
        
        # when list is empty
        if self.head is None:
            self.create_node(data)
            return
        
        # Insert at the beginning
        if pos == 0:
            pass # insert at head

        # Insert at last
        count = self.length()
        if pos == count:
            pass # insert at last

        # Insert at specific position
        temp = self.head
        prev = temp
        count = 1
        while temp:
            if count == pos:
                new_node = Node(data)
                prev.next = new_node
                new_node.next = temp
            count += 1
            prev = temp
            temp = temp.next                

    def print_prev_current(self):

        prev = None
        temp = self.head
        while temp:            
            print(f"(prev: {prev.data if prev is not None else "None"}, current: {temp.data})", end=" -> ")
            prev = temp
            temp = temp.next


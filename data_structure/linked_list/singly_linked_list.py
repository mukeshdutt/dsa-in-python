class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    ## Linked List Insertion

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

    ## Linked List Traversal

    def traversal_linked_list(self):

        temp = self.head
        while temp:
            print(f"{temp.data}", end=" -> ")
            temp = temp.next
        print("None")
    
    def print_prev_current(self):

        prev = None
        temp = self.head
        while temp:            
            print(f"(prev: {prev.data if prev is not None else "None"}, current: {temp.data})", end=" -> ")
            prev = temp
            temp = temp.next
    
    ## Delete from List
    def remove_from_head(self):
        self.head = self.head.next
    
    def remove_from_last(self):
        temp = self.head
        prev = None
        while temp:
            if temp.next is None:
                prev.next = None
                return
            prev = temp
            temp = temp.next
    
    def remove_from_a_position(self, position):
        
        ## Incase of empty linked list
        if self.head is None:
            return
        
        ## Incase of position 0
        temp = self.head
        if position == 0:
            self.head = temp.next
            return

        ## Incase of a specific position
        prev = None
        for _ in range(position):
            prev = temp
            temp = temp.next
            if temp.next is None:
                return
        
        prev.next = temp.next
        temp = None

    def operations():

        singly_linked_list = SinglyLinkedList()

        # create nodes
        singly_linked_list.create_node(2)
        singly_linked_list.create_node(4)
        singly_linked_list.create_node(8)
        singly_linked_list.create_node(10)
        singly_linked_list.create_node(12)
        
        # Insert at begin & end
        # singly_linked_list.insert_at_begin(10)
        # singly_linked_list.insert_at_end(14)
        # singly_linked_list.insert_at_end(14)

        # Insert at a position
        # singly_linked_list.insert_at_postion(2, 1001)
        
        singly_linked_list.traversal_linked_list()

        # singly_linked_list.remove_from_last()
        singly_linked_list.remove_from_a_position(3)
        singly_linked_list.traversal_linked_list()
from doubly_linked_list import Node, DoublyLinkedList

doubly_linked_list = DoublyLinkedList()

doubly_linked_list.create_node(2)
doubly_linked_list.create_node(4)
doubly_linked_list.create_node(6)
doubly_linked_list.create_node(8)
doubly_linked_list.create_node(10)
doubly_linked_list.insert_at_end(20)
doubly_linked_list.insert_at_position(101, 3)

doubly_linked_list.traversal_forward()

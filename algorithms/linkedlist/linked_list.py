from Node import Node

class Linked_List():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __len__(self):
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length
    
    def __str__(self):
        current = self.head
        output = "[" + str(current)
        current = current.next
        while current:
            output += ", " + str(current)
            current = current.next
        output += "]"
        return output

    def push(self, value):
        node = Node(value)
        if self.head is None:
            self.tail = node
            self.head = node
            return
        node.next = self.head
        self.head = node
    
    def append(self, value):
        node = Node(value)
        if self.tail is None:
            self.tail = node
            self.head = node
            return
        self.tail.next = node
        self.tail = node
        
    def append_multiple(self, vals):
        for val in vals:
            self.append(val)
    
    def push_multiple(self, vals):
        for val in vals:
            self.push(val)
    
    def pop(self):
        if self.head and self.head.next is None:
            self.head = None
            self.tail = None
            return
        if self.head:
            self.head = self.head.next
        else:
            return False
    
    def test_list(self, lst):
        current = self.head
        for val in lst:
            if current is None:
                return False
            if current.val != val:
                return False
            current = current.next
        return current == None
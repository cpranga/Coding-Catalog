class Stack:
    class StackNode:
        def __init__(self, val = None, next = None):
            self.val = val
            self.next = next
        def __str__(self):
            return str(self.val)
    
    def __init__(self, vals = None):
        self.head = None
        for val in vals:
            self.append(val)
    
    def __str__(self):
        if self.head is None:
            return "[]"
        
        node = self
        text = "[" + str(node.pop())
        while node:
            text += ", " + str(node.pop())
        text += "]"
        return text
    
    def __len__(self):
        copy = self.head
        leng = 0
        while copy:
            leng += 1
            copy = copy.next
        return leng
    
    def append(self, val):
        new_node = self.StackNode(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def peak(self):
        if self.head is None:
            return None
        return self.head.val
    
    def pop(self):
        if self.head is None:
            return None
        popped_val = self.head.val
        self.head = self.head.next
        return popped_val

if __name__ == "__main__":
    stack = Stack([1,2,3,4,5,6,7])
    print(stack)
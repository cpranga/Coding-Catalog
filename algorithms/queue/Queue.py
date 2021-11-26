class Queue:
    class QueueNode():
        def __init__(self, val, next = None):
            self.val = val
            self.next = next
    
    def __init__(self, vals = None):
        self.head = None
        self.tail = None
        for val in vals:
            self.append(val)
    
    def __len__(self):
        node = self.head
        leng = 0
        while node:
            leng += 1
            node = node.next
        return leng
    
    def __str__(self):
        if self.head is None:
            return "[]"
        
        node = self
        text = "[" + str(node.pop())
        while node:
            text += ", " + str(node.pop())
        text += "]"
        return text

    def append(self, val):
        new_node = self.QueueNode(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
    
    def pop(self):
        if self.head is None:
            return None
        popped_val = self.head.val
        self.head = self.head.next
        return popped_val
    
    def peak(self):
        if self.head is None:
            return None
        return self.head.val

if __name__ == "__main__":
    queue = Queue([7,6,5,4,3,2,1])
    print(queue)

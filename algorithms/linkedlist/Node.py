class Node():
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)
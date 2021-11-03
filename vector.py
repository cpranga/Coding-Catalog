'''
Implementation of a Vector by using Python Lists
'''

class Vector:
    '''
    Initializer: takes in a size and optional vector to copy
    '''
    def __init__(self, capacity, copy = None):
        self.capacity = capacity
        self.data = []
        if copy:
            self.data = copy
    
    # Returns number of elements in Vector
    def size(self):
        return len(self.data)
    
    # Returns capacity (max number of elements)
    def capacity(self):
        return self.capacity
    
    def is_empty(self):
        return self.size() = 0
    
    # Add element to end of vector
    def append(self, val):
        if self.size + 1 > capacity:
            self.size += 16
        self.data.append(val):
    
    # Add element to beginning of Vector, which pushes others back
    def prepend(self, val):
        if self.size + 1 > capacity:
            self.size += 16
        temp_vector = Vector(16)
        temp_vector.append(val)
        for src_val in self.data:
            temp_vector.append(src_val)
        self.data = temp_vector
    
    
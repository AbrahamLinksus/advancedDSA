# using xor to save mem space for trees 

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def createTree(arr):
    
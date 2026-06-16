# create a level order tree with N marking missing child

class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def createTree(array, i=0):
    if i >= len(array): return None
    data = array[i]
    if data == 'N': return None
    newNode = node(data)
    newNode.left = createTree(array, 2*i + 1)
    newNode.right = createTree(array, 2*i + 2)
    return newNode


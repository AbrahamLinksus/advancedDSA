class node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

def createTree(array=[1,2,3,4,5,6,7,8,9], i=0):
    if i >= len(array): return None
    newNode = node(array[i])
    newNode.left = createTree(array, 2*i + 1)
    newNode.right = createTree(array, 2*i + 2)
    return newNode

def findInfection(root, infectedNode):
    if root is None: return None
 

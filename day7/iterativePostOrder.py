# to traverse a tree post order iteratively 

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def createTree(array=[1,2,3,4,5,6,7,8,9], i=0):
    if i >= len(array): return None
    newNode = node(array[i])
    newNode.left = createTree(array, 2*i + 1)
    newNode.right = createTree(array, 2*i + 2)
    return newNode

def iterativePostOrder(head):
    if head is None: return None
    stack = [head]
    while stack:
        current = stack.pop()
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
        print(current.data)
    return "done"

tree1 = createTree()
iterativePostOrder(tree1)


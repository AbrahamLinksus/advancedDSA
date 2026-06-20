class node:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None

def createTree(dataArray=[1,2,3,4,5,6,7,8,9], i=0):
    if i >= len(dataArray): return None
    newNode = node(dataArray[i])
    newNode.left = createTree(dataArray, 2*i + 1)
    newNode.right = createTree(dataArray, 2*i + 2)
    return newNode

def inOrderTraverseByRecursion(root):
    if not root: return None
    inOrderTraverseByRecursion(root.left)
    print(root.val)
    inOrderTraverseByRecursion(root.right)

def inOrderTraverseByIteration(root):
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        if stack:
            current = stack.pop()
        print(current.val)
        current = current.right

tree1 = createTree()
print(inOrderTraverseByIteration(tree1))
print()
print(inOrderTraverseByRecursion(tree1))            

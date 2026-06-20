class node:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None

def createTree(dataArray=[1,2,3,4,5,6,7,8,9], i=0):
    if i >= len(dataArray): return 
    newNode = node(dataArray[i])
    newNode.left = createTree(dataArray, 2*i + 1)
    newNode.right = createTree(dataArray, 2*i + 2)
    return newNode

def preorderTraverseByRecursion(root):
    if not root: return 
    print(root.val)
    preorderTraverseByRecursion(root.left)
    preorderTraverseByRecursion(root.right)

def preorderTraverseByIteration(root):
    if not root: return 
    stack = [root]
    while stack:
        current = stack.pop()
        print(current.val)
        if current.right: stack.append(current.right)
        if current.left: stack.append(current.left)
        

tree1 = createTree()
print(preorderTraverseByIteration(tree1))
print()
print(preorderTraverseByRecursion(tree1))
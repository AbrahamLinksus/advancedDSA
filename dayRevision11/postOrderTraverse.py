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

def postOrderTraversalByRecursion(root):
    if not root: return
    postOrderTraversalByRecursion(root.left)
    postOrderTraversalByRecursion(root.right)
    print(root.val)

def postOrderTraverseByIteration(root):
    if not root: return
    res = []
    stack = [root]
    while stack:
        current = stack.pop()
        res.append(current.val)
        if current.left: stack.append(current.left)
        if current.right: stack.append(current.right)
    res.reverse()
    return res

tree1 = createTree()
postOrderTraversalByRecursion(tree1)
print(postOrderTraverseByIteration(tree1))


        

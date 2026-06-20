# LEETCODE : 94
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

def inorderTraverse(root):
    res = []
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        res.append(current.val)
        current = current.right
    return res

inOrderTree = createTree()
print(inorderTraverse(inOrderTree))
            

    
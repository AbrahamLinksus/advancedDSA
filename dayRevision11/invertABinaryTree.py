# LEETCODE : 226
class node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.right = None

def createTree(dataArray=[1,2,3,4,5,6,7,8,9], i=0):
    if i >= len(dataArray): return None
    newNode = node(dataArray[i])
    newNode.left = createTree(dataArray, 2*i + 1)
    newNode.right = createTree(dataArray, 2*i + 2)
    return newNode

def invertBinaryTree(root):
    if not root: return None
    root.left, root.right = root.right, root.left
    invertBinaryTree(root.left)
    invertBinaryTree(root.right)
    return root

def inOrderPrint(root):
    if not root: return None
    inOrderPrint(root.left)
    print(root.val)
    inOrderPrint(root.right)

tree1 = createTree()
print(inOrderPrint(tree1))
invertBinaryTree(tree1)
print(inOrderPrint(tree1))
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def createTree(array=[1,None,2,3,4,None,5], i=0):
    if i >= len(array): return None
    newNode = node(array[i])
    newNode.left = createTree(array, 2*i + 1)
    newNode.right = createTree(array, 2*i + 2)
    return newNode

def findHeight(root):
    if root is None: return 0
    leftHeight = findHeight(root.left)
    rightHeight = findHeight(root.right)
    return 1 + max(leftHeight, rightHeight)

def findDepth(root, label, depth=0, side=None):
    if root is None: return None
    if root.data == label: return depth, side
    left = findDepth(root.left,label ,1 + depth, side or "l")
    right = findDepth(root.right, label, 1 + depth, side or "r")
    return left or right

def findInfection(root, label):
    def helper(node):
        if node is None: return None, 0
        if node.data == label: return 0, findHeight(node) - 1
        leftDepth, leftBest = helper(node.left)
        rightDepth, rightBest = helper(node.right)
        if leftDepth is not None:
            depth = leftDepth + 1
            return depth, max(leftBest, depth + findHeight(node.right))
        if rightDepth is not None:
            depth = rightDepth + 1
            return depth, max(rightBest, depth + findHeight(node.left))
        return None, 0
    _, best = helper(root)
    return best


tree1 = createTree()
tree1.right.right.right = node(10)
tree1.right.right.right.right = node(11)
tree1.right.right.right.right.right = node(12)
print(findHeight(tree1))
print(findDepth(tree1, 4))
print(findInfection(tree1, 4))

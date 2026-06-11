# to find the height and diameter of a tree

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def createTree(dataArray, i=0):
    if i >= len(dataArray): return None
    node1 = node(dataArray[i])
    node1.left = createTree(dataArray, 2*i+1)
    node1.right = createTree(dataArray, 2*i+2)
    return node1

def printTree(head):
    if head is None: return None
    printTree(head.left)
    print(head.data)
    printTree(head.right)

def findHeight(head):
    if head is None: return -1
    leftHeight = findHeight(head.left)
    rightHeight = findHeight(head.right)
    return 1 + max(leftHeight, rightHeight)

def findDiameter(head):
    if head is None: return 0, 0

    lh, ld = findDiameter(head.left)
    rh, rd = findDiameter(head.right)
    height = 1 + max(lh, rh)
    diameter = max(lh + rh, ld, rd)

    return height, diameter


tree1 = createTree([1,2,3,4,5,6,7,8])
printTree(tree1)
print(findHeight(tree1))
print(findDiameter(tree1))
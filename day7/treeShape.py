# to find basic details about a tree

dataArray = [1, 2, 3, 4, 5, 6, 7]
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def createTree(dataArray, i=0):
    if i >= len(dataArray): return None
    node1 = node(dataArray[i])
    node1.left = createTree(dataArray, 2*i + 1)
    node1.right = createTree(dataArray, 2*i + 2)
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

def findLeafNodes(head):
    if head is None: return 0
    if head.left is None and head.right is None: return 1
    return findLeafNodes(head.left) + findLeafNodes(head.right)

def findInternalNodes(head):
    if head is None: return 0
    if head.left is None and head.right is None: return 0
    return 1 + findInternalNodes(head.left) + findInternalNodes(head.right)

tree1 = createTree(dataArray)
printTree(tree1)
print("Height of the tree is:", findHeight(tree1))
print("The number of leaf nodes are:", findLeafNodes(tree1))
print("Internal nodes: ", findInternalNodes(tree1))
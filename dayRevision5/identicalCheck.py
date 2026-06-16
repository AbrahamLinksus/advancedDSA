class node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

def createTree(array=[1,2,3,4,5,6,7,8,9], i=0):
    if i >= len(array): return None
    newNode = node(array[i])
    newNode.left = createTree(array, 2*i + 1)
    newNode.right = createTree(array, 2 * i + 2)
    return newNode

def checkIdentical(root1, root2):
    if root1 is None and root2 is None: return True
    if root1 is None or root2 is None: return False
    return (root1.data == root2.data) and checkIdentical(root1.left, root2.left) and checkIdentical(root1.right, root2.right)

tree1 = createTree()
tree2 = createTree()
print(checkIdentical(tree1, tree2))


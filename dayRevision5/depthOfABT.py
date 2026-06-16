class node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None 

def createTree(array=[1,2,3,4,5,6,7,8,9], i=0):
    if i >= len(array): return None
    newNode = node(array[i])
    newNode.left = createTree(array, 2*i + 1)
    newNode.right = createTree(array, 2*i + 2)
    return newNode

def findDiameter(root):
    if root is None: return 0, 0
    lh, ld = findDiameter(root.left)
    rh, rd = findDiameter(root.right)
    height = 1 + max(lh, rh)
    diameter = max(lh + rh, ld, rd)
    return diameter, height

def viewTree(root):
    if root is None: return None
    viewTree(root.left)
    print(root.data)
    viewTree(root.right)

tree1 = createTree()
print(viewTree(tree1))
print(findDiameter((tree1)))



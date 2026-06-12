# to traverse a tree

dataArray = [4, 2, 6, 1, 3, 5, 7]

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

def viewLevelOrder(root):
    if root is None: return None
    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.data)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return "done"

def viewInOrder(root):
    if root is None: return 0,0
    leftVal, leftCount = viewInOrder(root.left)
    print(root.data)
    rightVal, rightCount = viewInOrder(root.right)
    return root.data+leftVal+rightVal, 1+leftCount+rightCount

        

tree1 = createTree(dataArray)
print(viewInOrder(tree1))

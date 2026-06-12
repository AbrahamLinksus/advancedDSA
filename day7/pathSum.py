# to calculate the root to leaf path of a binary tree, 
# find the maximum number of root to leaf paths, and count the number of path that reach a target

class node:
    def __init__(self, data):
        self.data = data 
        self.left= None
        self.right = None

def createTree(array=[1,2,3,4,5,6,7,8,9], i=0):
    if i >= len(array): return None
    newNode = node(array[i])
    newNode.left = createTree(array, 2*i + 1)
    newNode.right = createTree(array, 2*i + 2)
    return newNode

def pathSum(head, target):
    if head is None: return None
    stack = [head]
    pathToTarget = pathToLeaf = 0
    while stack:
        current = stack.pop()
        if current.left is None and current.right is None:
            pathToLeaf += 1
            if current.data == target:
                pathToTarget += 1
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
        
    return pathToLeaf, pathToTarget

def findSums(head):
    if head is None: return -1
    if head.left is None and head.right is None: return head.data
    leftSum = findSums(head.left)
    rightSum = findSums(head.right)
    return max(leftSum, rightSum) + head.data

tree1 = createTree()
print(pathSum(tree1, 9))
print(findSums(tree1))
        


#if current is None, return None
# if current == leftval || current == rightVal, return current
#left = findcommonancestor(current.left), right = findcommonancestor(common,right)
#if left is None, return right 
#if left and right, return current

class node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

def createTree(array=[1,2,3,4,5,6,7,8,9], i=0):
    if i >= len(array): return None
    newNode = node(array[i])
    newNode.left = createTree(array, 2*i + 1)
    newNode.right = createTree(array, 2*i + 2)
    return newNode

def findLowestCommonAncestor(head, label1, label2):
    if head is None: return None
    if head.data == label1 or head.data == label2: return head.data

    leftTree = findLowestCommonAncestor(head.left, label1, label2)
    rightTree = findLowestCommonAncestor(head.right, label1, label2)
    if leftTree and rightTree: return head.data
    return leftTree or rightTree
    


tree1 = createTree()
print(findLowestCommonAncestor(tree1, 8, 5))

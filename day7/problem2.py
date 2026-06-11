#compare height with the depth 

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def createTree(inorder, preorder):
    if not inorder or not preorder: return None
    root = preorder.pop(0)
    index = inorder.index(root)
    node1 = node(root)
    node1.left = createTree(inorder[:index], preorder)
    node1.right = createTree(inorder[index+1:], preorder)
    return node1

def printTree(head):
    if not head: return None
    queue = [head]
    while queue:
        current = queue.pop(0)
        print(current.data)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return

def findHeight(head):
    if head is None: return -1
    leftHeight = findHeight(head.left)
    rightHeight = findHeight(head.right)
    return 1 + max(leftHeight, rightHeight)

def findDepth(head, label, depth=0):
    if head is None: return -1
    if head.data == label: return depth
    leftTree = findDepth(head.left, label, depth + 1)
    rightTree = findDepth(head.right, label, depth + 1)
    if leftTree == -1: return rightTree
    return leftTree

tree1 = createTree(["A", "B", "C", "D", "E", "F", "G", "H"], ["D","B","A","C","E","F", "G", "H"])
tree2 = createTree(["A", "B", "C", "D", "E", "F"], ["A", "B", "C", "D", "E", "F"])
printTree(tree1)
print(findHeight(tree1))
print(findDepth(tree1, "G"))
print()
print(findHeight(tree2))
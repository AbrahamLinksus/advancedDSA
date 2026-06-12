# to traverse a tree iteratively, pre order 

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def createTree(array, i=0):
    if i >= len(array): return None
    newNode = node(array[i])
    newNode.left = createTree(array, 2*i + 1)
    newNode.right = createTree(array, 2*i + 2)
    return newNode

def traverse(head):
    while head is None: return None
    print(head.data)
    traverse(head.left)
    traverse(head.right)

def iterativePreOrder(head):
    stack = [head]
    while stack:
        current = stack.pop()
        print(current.data)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return "done"

tree1 = createTree([1,2,3,4,5,6,7,8,9])
iterativePreOrder(tree1)
print()
traverse(tree1)

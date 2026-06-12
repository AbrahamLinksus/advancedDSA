# to find the in-order, pre-order and post-order in one traversal 

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def createTree(dataArray, i=0):
    if i >= len(dataArray): return None
    newNode = node(dataArray[i])
    newNode.left = createTree(dataArray, 2*i + 1)
    newNode.right = createTree(dataArray, 2*i + 2)
    return newNode

def traverseAll(head):
    if head is None: return None
    stack = [(head, 1)]
    preOrder = []
    inOrder = []
    postOrder = []
    while stack:
        current, state = stack.pop()
        if state == 1:
            preOrder.append(current.data)
            stack.append((current, 2))
            if current.left:
                stack.append((current.left, 1))
        elif state == 2:
            inOrder.append(current.data)
            stack.append((current, 3))
            if current.right:
                stack.append((current.right,1))
        else:
            postOrder.append((current.data))

    return preOrder, inOrder, postOrder

tree1 = createTree([1,2,3,4,5,6,7,8,9])
print(traverseAll(tree1))
class node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

def createTree(array=[1,2,3,4,5,6,7,8,9], i=0):
    if i >= len(array): return None
    newNode = node(array[i])
    newNode.left = createTree(array,2*i + 1)
    newNode.right = createTree(array, 2* i + 2)
    return newNode

def zigZagTraverse(root):
    if root is None: return None
    queue = [root]
    reverse = False
    while queue:
        if reverse:
            current = queue.pop(0)
            print(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        else:
            current = queue.pop()
            print(current.data)
            if current.left:
                queue.insert(0, current.left)
            if current.right:
                queue.insert(0, current.right)
        reverse = not reverse

tree1 = createTree()
zigZagTraverse(tree1)

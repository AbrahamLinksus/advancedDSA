# to find the top view, bottom, left and right view 

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

def findTopView(head, axis=0):
    if head is None: return None
    visitedHash = {}
    


    return

def findBottomView(head):
    return

def findRightView(head):
    if head is None: return None
    res = []
    queue = [head]
    while queue:
        length = len(queue)
        for index in range(length):
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            if index == length - 1:
                res.append(current.data)
    return res

def findLeftView(head):
    if head is None: return None
    res = []
    queue = [head]
    while queue:
        length = len(queue)
        for index in range(length):
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            if index == 0: res.append(current.data)
    return res

tree1 = createTree()
print("Right View: ",findRightView(tree1))

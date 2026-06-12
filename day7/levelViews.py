# to find the level views of a tree 
# problem 2 - 1 
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def createTree(array=[1,2,3,4,5,6, 7, 8, 9], i=0):
    if i >= len(array): return None
    newNode = node(array[i])
    newNode.left = createTree(array, 2*i + 1)
    newNode.right = createTree(array, 2*i + 2)
    return newNode

def rightView(head):
    if head is None: return None
    queue = [head]
    res = []
    maxSum = float("-inf")
    sum = 0
    while queue:
        length = len(queue)
        for index in range(length):
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            print(sum)
            sum += current.data
            if index == length - 1:
                res.append(current.data)
        maxSum = max(maxSum, sum)
        sum = 0
    return res, maxSum

    
tree1 = createTree()
print(rightView(tree1))
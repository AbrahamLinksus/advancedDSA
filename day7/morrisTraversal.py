# morris traversal

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

def morrisTraverse(head):
    current = head
    while current:                                          # check if im not in the end 
        if current.left is None:                            # if there is nothing to my left, means ill have to process myself and move right 
            print(current.data)
            current = current.right  
        else:                                               # if there is something to my left then, 
            prev = current.left                             # move to the rightmost end of the left sub tree
            while prev.right and prev.right != current:
                prev = prev.right

            if prev.right is None:                          # if rightmost is None, then it means i havent visited
                prev.right = current
                current = current.left

            else:                                           # if it is current, then this is my second time visiting here, so i cut the thread and move right 
                prev.right = None
                print(current.data)
                current = current.right

def printTree(head):
    if head is None: return None
    printTree(head.left)
    print(head.data)
    printTree(head.right)

tree1 = createTree([1,2,3,4,5,6,7])
morrisTraverse(tree1)
print()
printTree(tree1)


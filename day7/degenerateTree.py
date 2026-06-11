# when the inorder and preorder values are same, a degenerate tree is made(skewed)

inOrder = ["D", "B", "E", "A", "F", "C"]
preOrder = ["D", "B", "E", "A", "F", "C"]

class node:
      def __init__(self, data):
          self.data = data
          self.left = None
          self.right = None


def inOrderTree(dataArray, preOrder):
      if not dataArray or not preOrder: return None
      root = preOrder.pop(0)       
      i = dataArray.index(root)     
      newNode = node(root)
      newNode.left = inOrderTree(dataArray[:i], preOrder)
      newNode.right = inOrderTree(dataArray[i+1:], preOrder)
      return newNode

def traverseBFS(head):
    if head is None: return 0
    queue = [head]
    while queue:
        current = queue.pop(0)
        print(current.data)
        if current.left:
             queue.append(current.left)
        if current.right:
             queue.append(current.right)
    return 

         
tree1 = inOrderTree(inOrder, preOrder)
traverseBFS(tree1)





    



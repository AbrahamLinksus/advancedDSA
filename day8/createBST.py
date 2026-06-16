class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

class createBST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val):
        def _ins(node, val):
            if node is None: return Node(val)
            if val < node.val: node.left = _ins(node.left, val)
            elif val > node.val: node.right = _ins(node.right, val)
            return node
        self.root = _ins(self.root, val)

    def search(self, val):
        node = self.root
        while node:
            if val == node.val: return True
            node = node.left if val < node.val else node.right
        return False

bst = createBST()
for element in range(9):
    bst.insert(element)

bst.search(4)
bst.search(6)
bst.search(11)

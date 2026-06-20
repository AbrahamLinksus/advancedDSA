# FLOOR and CEIL in a BST

def findFloor(root, target):
    candidate = None    
    while root:
        if root.val == target:
            return target
        elif root.val > target:
            root = root.left
        else:
            candidate = root.val
            root = root.right
    return candidate

def findCeil(root, target):
    candidate = None
    while root:
        if root.val == target:
            return target
        elif root.val < target:
            root = root.right
        else:
            candidate = root.val
            root = root.left
    return candidate


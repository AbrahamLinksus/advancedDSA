# LEETCODE : 98

def isValidBST(root, minVal=float('-inf'), maxVal=float('inf')):
    if not root: return True
    if not (minVal < root.val < maxVal): return False
    return (isValidBST(root.left, minVal, root.val) and isValidBST(root.right, root.val, maxVal))


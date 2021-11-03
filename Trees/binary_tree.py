class TreeNode():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

def min_branch(root):
    if root is None:
        return 0
    return min(min_branch(root.left) + 1, min_branch(root.right) + 1)

def max_branch(root):
    if root is None:
        return 0
    return max(max_branch(root.left) + 1, max_branch(root.right) + 1)
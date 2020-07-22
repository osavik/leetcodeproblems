from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if p is None and q is None:
            return True
        elif p is None or q is None or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and \
        self.isSameTree(p.right, q.right)


# TIME: O(n)
# SPACE O(log n) best, average O(n)
        
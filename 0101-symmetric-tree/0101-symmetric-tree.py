# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        return self.isMirror(root.left,root.right)
    def isMirror(self,a,b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        return(
            a.val==b.val and
            self.isMirror(a.left,b.right) and
            self.isMirror(a.right,b.left)
        )
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        # while root:
        #Recursive
        # if not root or root.val==val:
        #     return root
        # if val<root.val:
        #     return self.searchBST(root.left,val)
        # else:
        #     return self.searchBST(root.right,val)
        # #Iterative:
        cur=root
        while cur:
            if cur.val==val:
                return cur
            cur=cur.left if val<cur.val else cur.right
            
        return None
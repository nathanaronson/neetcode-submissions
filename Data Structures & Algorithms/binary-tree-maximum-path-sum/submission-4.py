# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
    
        def helper(node):
            nonlocal res

            if not node:
                return 0

            left, right = max(helper(node.left), 0), max(helper(node.right), 0)
            res = max(res, node.val + left + right)
            return node.val + max(left, right)
        
        helper(root)
        return res
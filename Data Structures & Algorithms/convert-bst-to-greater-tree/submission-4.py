# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sys.setrecursionlimit(10**6)

        def helper(node, curr):
            if not node:
                return curr
            
            res = helper(node.right, curr)
            node.val += res
            return helper(node.left, node.val)
        
        helper(root, 0)
        return root
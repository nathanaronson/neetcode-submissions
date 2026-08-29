# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.helper(root, -101)
        
    def helper(self, curr, max_v):
        if not curr:
            return 0

        good = 1 if curr.val >= max_v else 0
        max_v = max(max_v, curr.val)
        return good + self.helper(curr.left, max_v) + self.helper(curr.right, max_v)
        
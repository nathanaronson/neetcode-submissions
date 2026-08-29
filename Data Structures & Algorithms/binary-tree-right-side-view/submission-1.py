# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        in_order = []
        def helper(node, depth):
            if not node:
                return

            nonlocal in_order
            if len(in_order) <= depth:
                in_order.append([node.val])
            else:
                in_order[depth].append(node.val)
            helper(node.left, depth + 1)
            helper(node.right, depth + 1)

        helper(root, 0)
        return [row[-1] for row in in_order]
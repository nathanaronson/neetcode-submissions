# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        data = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                data.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                data.append('#')
        
        return ','.join(data)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(',')

        if nodes[0] == '#':
            return None
        
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        i = 1
        
        while queue:
            node = queue.popleft()

            if i < len(nodes) and nodes[i] != '#':
                node.left = TreeNode(int(nodes[i]))
                queue.append(node.left)
            i += 1

            if i < len(nodes) and nodes[i] != '#':
                node.right = TreeNode(int(nodes[i]))
                queue.append(node.right)
            i += 1
        
        return root
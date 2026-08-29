"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        created = {}

        def copy(node):
            nonlocal created

            if not node:
                return None

            new = Node(node.val)
            new.neighbors = []
            created[node] = new

            for neighbor in node.neighbors:
                if neighbor not in created:
                    new.neighbors.append(copy(neighbor))
                else:
                    new.neighbors.append(created[neighbor])
                    
            return new
        
        return copy(node)
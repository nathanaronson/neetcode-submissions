# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from dataclasses import dataclass

@dataclass
class Node:
    node: ListNode

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [Node(node) for node in lists if node]
        heapq.heapify(heap)

        dummy = prev = ListNode()

        while heap:
            x = heapq.heappop(heap)
            node = x.node
            prev.next = node
            prev = prev.next
            if node.next:
                heapq.heappush(heap, Node(node.next))
        
        return dummy.next
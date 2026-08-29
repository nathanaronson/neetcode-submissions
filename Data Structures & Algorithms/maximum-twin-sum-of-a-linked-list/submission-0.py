# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        idx = {}

        i = 0
        while head:
            idx[i] = head.val
            head = head.next
            i += 1
        
        best = 0
        for i in range(len(idx) // 2):
            best = max(best, idx[i] + idx[len(idx) - i - 1])
        
        return best
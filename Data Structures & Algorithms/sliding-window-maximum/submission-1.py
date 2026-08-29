class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = [(nums[i], i) for i in range(k)]
        heapq.heapify_max(heap)
        res.append(heap[0][0])
        for i in range(k, len(nums)):
            heapq.heappush_max(heap, (nums[i], i))
            while heap[0][1] < i - k + 1:
                heapq.heappop_max(heap)
            res.append(heap[0][0])
        
        return res
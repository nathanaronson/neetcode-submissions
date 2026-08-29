class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [-cnt for cnt in freq.values()]
        heapq.heapify(heap)
        t = 0
        queue = deque()

        while heap or queue:
            t += 1
            if queue and queue[0][0] <= t:
                heapq.heappush(heap, queue.popleft()[1])
            if heap:
                count = heapq.heappop(heap) + 1
                if count < 0:
                    queue.append((t + n + 1, count))
        
        return t
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [-cnt for cnt in freq.values()]
        heapq.heapify(heap)
        cooldown = deque()
        t = 0
        while heap or cooldown:
            t += 1
            if cooldown and cooldown[0][0] == t:
                heapq.heappush(heap, cooldown.popleft()[1])
            if heap:
                count = heapq.heappop(heap) + 1
                if count < 0:
                    cooldown.append((t + n + 1, count))
        return t
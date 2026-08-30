class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(eq, pt, i) for i, (eq, pt) in enumerate(tasks)]
        tasks.sort()
        tasks = deque(tasks)
        time, pt, i = tasks.popleft()
        heap = [(pt, i)]
        result = []

        while heap:
            processing_time, index = heapq.heappop(heap)
            result.append(index)
            time = max(tasks[0][0] if tasks else 0, time + processing_time)

            while tasks and tasks[0][0] <= time:
                _, p, idx = tasks.popleft()
                heapq.heappush(heap, (p, idx))

        return result
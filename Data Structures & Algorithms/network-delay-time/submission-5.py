class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((v, w))

        distances = [(0, k)]
        visited = set()
        t = 0

        while distances:
            d, v = heapq.heappop(distances)

            if v in visited:
                continue

            visited.add(v)
            t = d
            
            for (u, w) in adj_list[v]:
                if u not in visited:
                    heapq.heappush(distances, (d + w, u))

        return t if len(visited) == n else -1
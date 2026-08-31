class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # can afford max heap -> profits
        # can't afford min heap -> capital, profits
        
        afford, cant_afford = [p for p, c in zip(profits, capital) if c <= w], [(c, p) for p, c in zip(profits, capital) if c > w]
        heapq.heapify_max(afford)
        heapq.heapify(cant_afford)

        for _ in range(k):
            if not afford:
                return w

            w += heapq.heappop_max(afford)

            while cant_afford and cant_afford[0][0] <= w:
                heapq.heappush_max(afford, heapq.heappop(cant_afford)[1])
        
        return w
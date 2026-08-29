class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        for point in points:
            x, y = point[0], point[1]
            dist = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush_max(closest, (dist, point))
            if len(closest) > k:
                heapq.heappop_max(closest)
        
        return [point for _, point in closest]
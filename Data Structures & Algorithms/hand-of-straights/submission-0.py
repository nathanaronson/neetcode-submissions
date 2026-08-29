class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = Counter(hand)
        heap = [(k, v) for k, v in freq.items()]
        heapq.heapify(heap)

        while heap:
            group = []

            for i in range(groupSize):
                if not heap:
                    return False
                k, v = heapq.heappop(heap)
                print((k, v))
                if group and k - 1 != group[-1][0]:
                    return False
                group.append((k, v - 1))
            
            for k, v in group:
                if v > 0:
                    heapq.heappush(heap, (k, v))

        return True
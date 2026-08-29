class MedianFinder:

    def __init__(self):
        self.left, self.right = [], []

    def addNum(self, num: int) -> None:
        left, right = self.left[0] if self.left else 0, self.right[0] if self.right else 0
        if num <= left:
            heapq.heappush_max(self.left, num)
        else:
            heapq.heappush(self.right, num)

        n, m = len(self.left), len(self.right)
        if abs(n - m) <= 1:
            return

        if n > m:
            heapq.heappush(self.right, heapq.heappop_max(self.left))
        else:
            heapq.heappush_max(self.left, heapq.heappop(self.right))

    def findMedian(self) -> float:
        if not self.left and not self.right:
            return 0
        
        n, m = len(self.left), len(self.right)
        if n == m:
            return (self.left[0] + self.right[0]) / 2
        elif n > m:
            return self.left[0]
        else:
            return self.right[0]
        
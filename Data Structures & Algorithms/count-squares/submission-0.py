class CountSquares:

    def __init__(self):
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        total = 0
        for (x2, y2), count in self.points.items():
            if abs(x1 - x2) != abs(y1 - y2) or x1 == x2 or y1 == y2:
                continue
            total += count * self.points[(x1, y2)] * self.points[(x2, y1)]
        return total

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        fleets = 1
        prev = (target - pair[0][0]) / pair[0][1]
        for i in range(1, len(pair)):
            p, s = pair[i]
            curr = (target - p) / s
            if curr > prev:
                prev = curr
                fleets += 1
        return fleets
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)

        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0

        visited = {"0000"}
        queue = deque([("0000", 0)])
        while queue:
            code, turns = queue.popleft()
            if code == target:
                return turns
            neighbors = set()
            for i in range(4):
                d = int(code[i])
                for j in ((d + 1) % 10, (d - 1) % 10):
                    neighbors.add(code[:i] + str(j) + code[i+1:])
            for i in neighbors:
                if i not in visited and i not in deadends:
                    visited.add(i)
                    queue.append((i, turns + 1))
        return -1

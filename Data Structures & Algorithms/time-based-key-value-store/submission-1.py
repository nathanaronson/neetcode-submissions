from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.values = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if len(self.values[key]) == 0:
            return ''
        
        i = self.values[key].bisect_right(timestamp)
        t = self.values[key].keys()[i - 1]

        if t > timestamp:
            return ''
        
        return self.values[key][t]
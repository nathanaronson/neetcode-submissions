class RandomizedSet:

    def __init__(self):
        self.values = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.values:
            return False
        self.values[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.values:
            return False
        i = self.values[val]
        self.arr[i], self.arr[-1] = self.arr[-1], self.arr[i]
        self.values[self.arr[i]] = i
        self.arr.pop()
        self.values.pop(val, None)
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
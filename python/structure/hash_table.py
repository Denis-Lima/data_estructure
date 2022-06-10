class HashMap:
    def __init__(self) -> None:
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key: str) -> int:
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def add(self, key: str, value):
        idx = self.get_hash(key)

        for index, element in enumerate(self.arr[idx]):
            if len(element) == 2 and element[0] == key:
                self.arr[idx][index] = (key, value)
                break
        else:
            self.arr[idx].append((key, value))

    def get(self, key: str):
        idx = self.get_hash(key)
        for element in self.arr[idx]:
            if element[0] == key:
                return element[1]
        return None

    def remove(self, key: str):
        idx = self.get_hash(key)
        for index, element in enumerate(self.arr[idx]):
            if element[0] == key:
                del self.arr[idx][index]

    def __setitem__(self, key: str, value):
        self.add(key, value)

    def __getitem__(self, key: str):
        return self.get(key)

    def __delitem__(self, key: str):
        self.remove(key)

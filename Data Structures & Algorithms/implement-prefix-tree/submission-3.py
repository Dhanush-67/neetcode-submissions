class PrefixTree:

    def __init__(self):
        self.arr = [None]*26
        self.isEnd = False

    def insert(self, word: str) -> None:

        for c in word:
            index = ord(c) - ord('a')
            if self.arr[index] == None:
                self.arr[index] = PrefixTree()
            self = self.arr[index]

        self.isEnd = True

    def search(self, word: str) -> bool:
        for c in word:
            index = ord(c) - ord('a')
            if self.arr[index] == None:
                return False
            self = self.arr[index]

        return self.isEnd

    def startsWith(self, prefix: str) -> bool:
        for c in prefix:
            index = ord(c) - ord('a')
            if self.arr[index] == None:
                return False
            self = self.arr[index]

        return True
        
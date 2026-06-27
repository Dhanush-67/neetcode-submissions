class WordDictionary:

    def __init__(self):
        self.lst = [None]*26
        self.isEnd = False

    def addWord(self, word: str) -> None:
        for c in word:
            index = ord(c) - ord('a')
            if self.lst[index] == None:
                self.lst[index] = WordDictionary()
            self = self.lst[index]
        self.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(num, root):
            for i in range(num, len(word)):
                char = word[i]

                if char == '.':
                    for j in range(26):
                        if root.lst[j] != None:
                            if dfs(i+1,root.lst[j]):
                                return True
                    return False
                else:
                    index = ord(char) - ord('a')
                    if root.lst[index] == None:
                        return False
                    root = root.lst[index]
            return root.isEnd

        return dfs(0, self)




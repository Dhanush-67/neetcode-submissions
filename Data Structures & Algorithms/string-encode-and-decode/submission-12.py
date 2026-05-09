class Solution:

    def encode(self, strs: List[str]) -> str:
        lst = []
        for s in strs:
            lst.append(str(len(s)) + "#" + s)
        return "".join(lst)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        length_s = len(s)

        while i < length_s:
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res


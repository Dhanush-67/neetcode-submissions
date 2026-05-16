class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)

        if length % 2 != 0:
            return False
        
        lst = []

        for i in range(length):
            if s[i] == "(":
                lst.append(")")
            elif s[i] == "[":
                lst.append("]")
            elif s[i] == "{":
                lst.append("}")
            elif lst and (s[i] == lst[-1]):
                lst.pop()
            else:
                return False
        
        if not lst:
            return True
        return False
        
        
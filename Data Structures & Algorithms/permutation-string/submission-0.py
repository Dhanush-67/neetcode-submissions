class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        l = 0
        r = 0

        dice = {}

        for x in s1:
            dice[x] = 1 + dice.get(x,0)

        while r < len(s2):
            stack = {}
            
            while r - l + 1 <= len(s1) and r < len(s2):
                stack[s2[r]] = 1 + stack.get(s2[r], 0)
                r += 1
            
            if stack == dice:
                return True
            l += 1
            r = l
        
        return False


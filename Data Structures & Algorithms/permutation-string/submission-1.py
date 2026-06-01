class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        l = 0
        r = 0
        l1 = len(s1)
        l2 = len(s2)

        dice = {}

        for x in s1:
            dice[x] = 1 + dice.get(x,0)

        while r < l2:
            stack = {}
            
            while r - l + 1 <= l1 and r < l2:
                stack[s2[r]] = 1 + stack.get(s2[r], 0)
                r += 1
            
            if stack == dice:
                return True
            l += 1
            r = l
        
        return False


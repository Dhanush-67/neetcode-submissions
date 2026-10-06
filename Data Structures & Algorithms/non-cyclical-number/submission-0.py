class Solution:
    def isHappy(self, n: int) -> bool:
        track = set()

        while (n != 1) and (n not in track):
            track.add(n)
            new = 0
            while n != 0:
                new += (n % 10)**2
                n //= 10
            n = new

        if n == 1:
            return True
        
        return False
        
class Solution:
    def isPalindrome(self, i, j, s):
        l,r = i,j
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            for j in range(i,len(s)):
                if self.isPalindrome(i,j,s):
                    count += 1

        return count

        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        l = 0
        r = l+1
        stack = set()
        stack.add(s[l])
        count = 1

        max_count = count

        while r < len(s):
            if not (s[r] in stack):
                stack.add(s[r])
                count += 1
                r += 1
            else:
                stack = set()
                l += 1
                r = l+1
                count = 1
                stack.add(s[l])

            max_count = max(count, max_count)
        
        return max_count
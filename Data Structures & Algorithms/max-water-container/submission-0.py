class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        length = len(heights)
        for i in range(length):
            for j in range(i + 1, length):
                res = max(res, min(heights[i], heights[j]) * (j - i))
        return res
        
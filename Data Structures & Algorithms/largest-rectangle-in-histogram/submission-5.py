class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        length = len(heights)

        for x in range(length):

            if heights[x] == 0:
                continue
    
            l = x-1
            r = x+1
            left_area = 0
            right_area = 0

            while l >= 0 and heights[l] >= heights[x]:
                left_area += 1
                l -= 1
            
            while r < length and heights[r] >= heights[x]:
                right_area += 1
                r += 1

            area = (right_area + left_area + 1)*heights[x]

            if area > max_area:
                max_area = area

        return max_area


        
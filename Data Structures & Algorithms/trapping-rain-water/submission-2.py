from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        max_height = max(height)
        length = len(height)

        if length <= 2:
            return water

        for i in range(max_height):
            s = set()
            for j in range(1,length-1):
                if j in s:
                    continue
                if(height[j]) > i:
                    continue
                l = j - 1
                r = j + 1
                water_left = 0
                water_right = 0

                fast_exit = 0
                while height[l] <= i:
                    fast_exit = 1
                    if l == 0 and height[l] <= i:
                        
                        water_left = -1
                        break
                    if l == 0:
                        break
                    s.add(l+1)
                    water_left += 1
                    l -= 1
                    fast_exit = 0

                if not(fast_exit):
                    s.add(l+1)
                    water_left += 1
                fast_exit = 0
                

                while height[r] <= i:
                    fast_exit = 1
                    if r == length-1 and height[r] <= i:
                        water_right = -1
                        break
                    if r == length-1:
                        break
                    s.add(r-1)
                    water_right += 1
                    r += 1
                    fast_exit = 0
                
                if not(fast_exit):
                    s.add(r-1)
                    water_right += 1

                if (water_left == -1) or (water_right == -1):
                    continue

            
                water += water_left + water_right - 1

        return water
        
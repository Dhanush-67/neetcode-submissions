class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def solve(start, end):
            cache = [-1] * len(nums)

            def dfs(num):
                if num >= end:
                    return 0

                if cache[num] != -1:
                    return cache[num]

                cache[num] = max(
                    dfs(num + 1),
                    nums[num] + dfs(num + 2)
                )
                return cache[num]

            return dfs(start)

        return max(
            solve(0, len(nums) - 1),  
            solve(1, len(nums))       
        )
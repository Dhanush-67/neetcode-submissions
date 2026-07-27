class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1]*len(nums)

        def dfs(num):
            if num > len(nums)-1:
                return 0

            if cache[num] != -1:
                return cache[num]
            else:
                cache[num] = max(nums[num]+dfs(num+2),dfs(num+1))

            return max(nums[num]+dfs(num+2),dfs(num+1))


        return dfs(0)

        for i in range(len(nums)):
            dfs(i)
        
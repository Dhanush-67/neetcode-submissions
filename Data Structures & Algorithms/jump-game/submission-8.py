class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        memo = [-1]*len(nums)

        def dfs(index):
            if index > target:
                return False
            if index == target:
                return True
            if nums[index] == 0:
                memo[index] = 0
                return False
            if memo[index] != -1:
                return memo[index] == 1

            for i in range(nums[index], 0, -1):

                if dfs(index+i):
                    memo[index] = 1
                    return True
            memo[index] = 0
            return False

        return dfs(0)
        
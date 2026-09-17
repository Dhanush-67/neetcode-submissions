class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:

        dic = {}

        def dfs(index, total):
            if index > len(nums):
                return 0
            if index == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if (index,total) in dic:
                return dic[(index,total)]

            dic[(index,total)] = dfs(index+1,total+nums[index]) + dfs(index+1,total+(nums[index]*-1))

            return dic[(index,total)]

        return dfs(0,0)
        
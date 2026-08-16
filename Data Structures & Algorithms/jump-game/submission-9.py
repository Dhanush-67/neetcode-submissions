class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = 0

        for i in range(len(nums)):
            if res < i:
                return False
            res = max(res,nums[i]+i)
        return True
        
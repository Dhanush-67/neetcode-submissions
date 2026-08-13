class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res  = nums[0]
        cur = 0
        for i in range(len(nums)):
            if cur + nums[i] >= nums[i]:
                cur = cur+nums[i]
            else:
                cur = nums[i]
            res = max(res,cur)


        return res

        
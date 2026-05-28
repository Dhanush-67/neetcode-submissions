class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = nums[0]

        for x in nums:
            if x < min:
                min = x
        return min
        
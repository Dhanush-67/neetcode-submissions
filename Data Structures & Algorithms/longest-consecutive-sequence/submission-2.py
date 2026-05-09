class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        count = 1
        lst = []

        if not nums:
            return 0

        for i in range(length-1):
            if(nums[i+1]-nums[i] == 1):
                count += 1
            elif(nums[i+1]-nums[i] == 0):
                continue
            else:
                lst.append(count)
                count = 1
        
        lst.append(count)
        return max(lst)
        
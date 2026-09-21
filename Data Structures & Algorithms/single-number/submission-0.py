class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}

        for num in nums:
            dic[num] = 1 + dic.get(num,0)

        for key in dic:
            if dic[key] == 1:
                return key
        
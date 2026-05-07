class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        dice = {}

        for i in range(length):
            dice[nums[i]] = 1 + dice.get(nums[i],0)

        lst = []

        for key in dice:
            lst.append(dice[key])
        
        lst.sort(reverse = True)

        final = []

        for i in range(k):
            for key in dice:
                if dice[key] == lst[i] and key not in final:
                    final.append(key)

        return final
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = {}
        for i in nums:
            track[i] = 1 + track.get(i,0)

        def dfs(index, subset):
            if len(subset) == len(nums):
                x = {}
                for i in subset:
                    x[i] = 1 + x.get(i,0)
                if x == track:
                    res.append(subset.copy())
                return
            if index >= len(nums):
                return

            for i in range(0,len(nums)):
                subset.append(nums[i])
                dfs(index+1, subset)
                subset.pop()
                dfs(index+1, subset)

        dfs(0, [])
        return res
        
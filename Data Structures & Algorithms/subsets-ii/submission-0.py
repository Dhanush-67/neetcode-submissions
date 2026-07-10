class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        track = set()

        def dfs(i, subset):
            if i >= len(nums):
                x = str(subset.copy())
                if x not in track:
                    res.append(subset.copy())
                    track.add(x)
                return
            
            subset.append(nums[i])
            dfs(i+1,subset)
            subset.pop()
            dfs(i+1, subset)

        dfs(0,[])
        return res
            
        
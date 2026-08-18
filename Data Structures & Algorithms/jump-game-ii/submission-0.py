class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dfs(index):
            if index >= n - 1:
                return 0                      # already at/past the end, 0 jumps needed
            if index in memo:
                return memo[index]

            best = float('inf')
            for i in range(nums[index], 0, -1):
                nxt = index + i
                if nxt <= n - 1:
                    sub = dfs(nxt)
                    if sub != float('inf'):
                        best = min(best, sub + 1)   # +1 for the jump we just took

            memo[index] = best
            return best

        return dfs(0)
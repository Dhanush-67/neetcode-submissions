class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        if amount == 0:
            return 0

        memo = {}

        def dfs(total):
            if total == 0:
                return 0
            
            if total < 0:
                return -1

            if total in memo:
                return memo[total]

            min_value = float('inf')
            flag = 0
            for i in range(len(coins)):
                isTrue = 1+dfs(total-coins[i])
                if isTrue:
                    min_value = min(min_value,isTrue)
                    flag = 1
            if flag:
                memo[total] = min_value
            else:
                memo[total] = -1
            return memo[total]

        coins.sort()
        coins.reverse()

        res = dfs(amount)
        if res:
            return res
        return -1
        
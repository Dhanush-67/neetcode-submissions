class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        dic = {}

        def dfs(index, flag):
            if index >= len(prices):
                return 0
            if (index, flag) in dic:
                return dic[(index, flag)]

            if flag == 1:
                # sell now (+price, then cooldown/skip) OR keep holding
                result = max(prices[index] + dfs(index+2, 0), dfs(index+1, 1))
            else:
                # buy now (-price) OR skip
                result = max(-prices[index] + dfs(index+1, 1), dfs(index+1, 0))

            dic[(index, flag)] = result
            return result

        return dfs(0, 0)
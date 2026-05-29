class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length == 1:
            return 0
        maxi = 0
        mini = prices[0]
        for i in range(length):
            j = i - 1
            if j >= 0:
                mini = min(mini, prices[j])
                maxi = max(maxi, prices[i] - mini)
        
        return maxi
            
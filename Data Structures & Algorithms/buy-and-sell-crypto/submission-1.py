class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        maxi = 0
        mini = prices[0]
        for i in range(len(prices)):
            j = i - 1
            if j >= 0:
                mini = min(mini, prices[j])
                maxi = max(maxi, prices[i] - mini)
        
        return maxi
            
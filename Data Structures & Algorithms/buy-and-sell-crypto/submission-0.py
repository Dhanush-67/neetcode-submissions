class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                if prices[i] < prices[j]:
                    maxi = max(maxi,prices[j]-prices[i])
        return maxi
        
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dic = {}
        def dfs(index,total):
            if index >= len(coins):
                return 0
            if total == amount:
                return 1
            if total > amount:
                return 0
            if (index,total) in dic:
                return dic[(index,total)]
            
            dic[(index,total)] = dfs(index,total+coins[index])+dfs(index+1,total)
            return dic[(index,total)]

        return dfs(0,0)
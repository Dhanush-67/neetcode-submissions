class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dic = {}

        def dfs(i1,i2):
            count1 = 0
            count2 = 0
            if i1 >= len(text1) or i2 >= len(text2):
                return 0

            if (i1,i2) in dic:
                return dic[(i1,i2)]
            if text1[i1] == text2[i2]:
                count1 = 1+dfs(i1+1,i2+1)
            else:
                count2 = max(dfs(i1+1,i2),dfs(i1,i2+1))

            dic[(i1,i2)] = max(count1,count2)
            return max(count1,count2)

        return dfs(0,0)

        
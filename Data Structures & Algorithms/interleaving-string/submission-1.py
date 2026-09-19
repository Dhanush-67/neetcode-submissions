class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False

        dic = {}


        def dfs(i,j,k):
            if k >= len(s3):
                return True

            if (i,j) in dic:
                return dic[(i,j)]

            if i < len(s1) and j < len(s2) and s3[k] == s1[i] and s3[k] == s2[j]:
                dic[(i,j)] = dfs(i+1,j,k+1) or dfs(i,j+1,k+1)
                return dic[(i,j)]
            if i < len(s1) and s3[k] == s1[i]:
                dic[(i,j)] = dfs(i+1,j,k+1)
                return dic[(i,j)]
            if j < len(s2) and s3[k] == s2[j]:
                dic[(i,j)] = dfs(i,j+1,k+1)
                return dic[(i,j)]

            return False

        return dfs(0,0,0)
        
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        res = []
        visited = set()

        def pacific_dfs(i, j, height, visited):
            if i<0 or j <0:
                return True
            if i >= m or j >= n or heights[i][j] > height or (i,j) in visited:
                return False
            
            visited.add((i,j))

            return pacific_dfs(i-1,j,heights[i][j], visited) or pacific_dfs(i,j-1,heights[i][j], visited) or pacific_dfs(i+1,j, heights[i][j], visited) or pacific_dfs(i,j+1, heights[i][j], visited)

        def atlantic_dfs(i, j, height, visited):
            if i>=m or j>=n:
                return True
            if i<0 or j <0 or heights[i][j] > height or (i,j) in visited:
                return False

            visited.add((i,j))

            return atlantic_dfs(i+1,j,heights[i][j], visited) or atlantic_dfs(i,j+1,heights[i][j], visited) or atlantic_dfs(i-1,j, heights[i][j], visited) or atlantic_dfs(i,j-1, heights[i][j], visited)

        for i in range(m):
            for j in range(n):
                if pacific_dfs(i,j,heights[i][j], set()) and atlantic_dfs(i,j,heights[i][j], set()):
                    res.append([i,j])

        return res


        
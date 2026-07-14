class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if (i,j) in visited or grid[j][i] == "0":
                return

            visited.add((i,j))

            if i - 1 >= 0:
                dfs(i-1,j)
            if j-1 >= 0:
                dfs(i, j-1)
            if i+1 < n:
                dfs(i+1,j)
            if j+1 < m:
                dfs(i,j+1)

            


        for i in range(m):
            for j in range(n):
                if (j,i) not in visited and grid[i][j] != "0":
                    dfs(j,i)
                    count += 1

        return count
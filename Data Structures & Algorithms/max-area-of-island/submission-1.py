class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        count = 0
        subcount = 0
        max_area = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            nonlocal subcount
            if (i,j) in visited or grid[j][i] == 0:
                return

            visited.add((i,j))
            subcount += 1

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
                subcount = 0
                if (j,i) not in visited and grid[i][j] != 0:
                    dfs(j,i)
                    max_area = max(max_area,subcount)


        return max_area
        
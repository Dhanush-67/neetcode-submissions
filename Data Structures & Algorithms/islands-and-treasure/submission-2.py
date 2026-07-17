class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        
        
        def bfs(i, j, visted):
            count = 0
            queue = deque()
            x,y = i,j
            queue.append((x,y,0))

            while queue:
                a1,a2,distance = queue.popleft()
                if grid[a1][a2] == 0:
                    grid[i][j] = distance
                    return
                
                visited.add((a1,a2))

                if a1-1>=0 and grid[a1-1][a2] != -1 and (a1-1,a2) not in visited:
                    queue.append((a1-1,a2,distance+1))
                if a2-1>=0 and grid[a1][a2-1] != -1 and (a1,a2-1) not in visited:
                    queue.append((a1,a2-1,distance+1))
                if a2+1<n and grid[a1][a2+1] != -1 and (a1,a2+1) not in visited:
                    queue.append((a1,a2+1,distance+1))
                if a1+1<m and grid[a1+1][a2] != -1 and (a1+1,a2) not in visited:
                    queue.append((a1+1,a2,distance+1))
                

        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1 and grid[i][j] != 0:
                    visited = set()
                    bfs(i,j,visited)
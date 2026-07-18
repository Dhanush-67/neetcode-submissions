class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rotten_stack = []
        count = 0
        minutes = -1

        def bfs(arr):
            nonlocal count
            nonlocal minutes
            queue = deque()
            for x in arr:
                queue.append(x)

            while queue:
                length = len(queue)
                for num in range(length):
                    i,j = queue.popleft()
                    if i-1 >= 0 and grid[i-1][j] == 1:
                        grid[i-1][j] = 2
                        count -= 1
                        queue.append((i-1,j))
                    if j-1 >= 0 and grid[i][j-1] == 1:
                        grid[i][j-1] = 2
                        count -= 1
                        queue.append((i,j-1))
                    if i+1 < m and grid[i+1][j] == 1:
                        grid[i+1][j] = 2
                        count -= 1
                        queue.append((i+1,j))
                    if j+1 < n and grid[i][j+1] == 1:
                        grid[i][j+1] = 2
                        count -= 1
                        queue.append((i,j+1))
                minutes += 1



        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten_stack.append((i,j))
                if grid[i][j] == 1:
                    count += 1
        
        if rotten_stack:
            bfs(rotten_stack)


        if count != 0:
            return -1
        elif count == 0 and not rotten_stack:
            return 0
        else:
            return minutes



        
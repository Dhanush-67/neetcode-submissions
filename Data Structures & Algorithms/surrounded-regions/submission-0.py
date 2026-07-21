class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        m = len(board)
        n = len(board[0])

        def dfs(i,j):
            if i < 0 or j < 0 or i >= m or j >= n or (i,j) in visited or board[i][j] == "X":
                return

            visited.add((i,j))
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i,j+1)

        for c in range(n):
            dfs(0,c)
            dfs(m-1,c)
        for r in range(m):
            dfs(r,0)
            dfs(r,n-1)

        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and board[i][j] == "O":
                    board[i][j] = "X"
            


        
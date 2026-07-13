class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = set()

        def dfs(index, x, y):
            # Entire word has been matched
            if index == len(word):
                return True

            # Out of bounds
            if x < 0 or x >= n or y < 0 or y >= m:
                return False

            # Wrong character or reused cell
            if board[y][x] != word[index] or (x, y) in visited:
                return False

            visited.add((x, y))

            found = (
                dfs(index + 1, x - 1, y) or
                dfs(index + 1, x + 1, y) or
                dfs(index + 1, x, y - 1) or
                dfs(index + 1, x, y + 1)
            )

            visited.remove((x, y))
            return found

        # The word can start at any board position
        for y in range(m):
            for x in range(n):
                if dfs(0, x, y):
                    return True

        return False
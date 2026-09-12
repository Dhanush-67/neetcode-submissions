class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for x in range(m-1):
            newRow = [1] * n
            for y in range(n-2,-1,-1):
                newRow[y] = newRow[y+1]+row[y]
            row = newRow

        return row[0]
        
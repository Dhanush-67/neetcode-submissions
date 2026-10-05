class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if not i in row:
                        row.add(i)
                    if not j in col:
                        col.add(j)

        for i in range(len(matrix)):
            if i in row:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j in col:
                    matrix[i][j] = 0

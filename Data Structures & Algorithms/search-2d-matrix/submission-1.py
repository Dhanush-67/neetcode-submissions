class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length = len(matrix)
        inner_length = len(matrix[0])
        last_index = inner_length - 1
        mid = -1

        l = 0
        r = length
        found = 0

        while l < r:
            mid = l + (r-l)//2

            if matrix[mid][0] <= target <= matrix[mid][last_index]:
                found = 1
                break
            elif target < matrix[mid][0]:
                r = mid
            else:
                l = mid + 1
        if found == 0:
            return False
        
        l = 0
        r = inner_length
        outer_index = mid

        while l < r:
            mid = l + (r - l) // 2

            if matrix[outer_index][mid] == target:
                return True
            elif matrix[outer_index][mid] < target:
                l = mid + 1
            else:
                r = mid
        return False
        
        
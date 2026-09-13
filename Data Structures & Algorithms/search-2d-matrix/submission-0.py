class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])

        top = 0
        bottom = r * c -1

        while top <= bottom: 
            m = top + ((bottom - top) // 2)
            row = m // c
            col = m % c
            if matrix[row][col] > target: 
                bottom = m - 1
            elif matrix[row][col] < target: 
                top = m + 1
            else:
                return True 
        return False


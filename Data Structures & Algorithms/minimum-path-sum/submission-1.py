class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        matrix = [[-1] * n for _ in range(m)]
        def helper(matrix, i, j):
            
            if i >= m or j >= n:
                return math.inf
            if matrix[i][j] != -1:
                return matrix[i][j]
            if i == m-1 and j == n-1:
                return grid[i][j]
            down = grid[i][j] + helper(matrix, i+1, j)
            right = grid[i][j] + helper(matrix, i, j+1)
            matrix[i][j] = min(down,right)
            return matrix[i][j]
            
        return helper(matrix, 0, 0)

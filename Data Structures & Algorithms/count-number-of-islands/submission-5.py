class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        def dfs(row, col):
            if row >= len(grid) or row < 0 or col >= len(grid[row]) or col < 0:
                return False
            if grid[row][col] == "0" or visited[row][col]:
                return False
                
            visited[row][col] = True

            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)
            
            
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1" and not visited[row][col]:
                    dfs(row,col)
                    islands+=1


        return islands
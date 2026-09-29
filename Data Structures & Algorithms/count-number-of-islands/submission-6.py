class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        queue = []
        
        def bfs(row, col):
            q = deque()
            q.append((row,col))

            while q:
                row, col = q.popleft()
                if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or grid[row][col] == "0" or visited[row][col]:
                    continue
                visited[row][col] = True
                q.append((row+1,col))
                q.append((row-1,col))
                q.append((row,col+1))
                q.append((row,col-1))

            
            
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1" and not visited[row][col]:
                    bfs(row,col)
                    islands+=1


        return islands
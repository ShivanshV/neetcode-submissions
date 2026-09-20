class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        print(visited)
        def helper(row, col, index):
            if index == len(word):
                return True

            if row < 0  or row >= len(board) or col < 0 or col >= len(board[row]) or visited[row][col] or board[row][col] != word[index]:
                return False
            
            
            
  
            visited[row][col] = True
            res =  helper(row+1,col, index+1) or helper(row-1,col, index+1) or helper(row,col-1, index+1) or helper(row,col+1, index+1)
            visited[row][col] = False
            return res
        
            
        for row in range(len(board)):
            for col in range(len(board[row])):
                if helper(row,col, 0):
                    return True

        return False
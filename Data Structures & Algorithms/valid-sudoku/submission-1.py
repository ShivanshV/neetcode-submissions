class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] != ".":
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] != ".":
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        for i in range(9):
            seen = set()
            for row in range(3):
                for col in range(3):
                    num = board[row+((i//3)*3)][col+((i%3)*3)]
                    if num != ".":
                        if num in seen:
                            return False
                        seen.add(num)

                
        return True



        #(0,0) (0,1) (0,2) (1,0) (1,1) (1,2) (2,0) (2,1) (2,2)
        #(0,3) 0      0     1     1     1    2     2     2
        #(0,6) 0
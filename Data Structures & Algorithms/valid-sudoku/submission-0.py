class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for i in range(9):
                if row[i] == ".":
                    continue
                if row[i] in seen:
                    return False
                else:
                    seen.add(row[i])
        
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                else:
                    seen.add(board[row][col])
        
        for box in range(9):
            seen = set()
            for row in range(3):
                for col in range(3):
                    
                    if board[(box//3)*3+row][(box%3)*3+col] == ".":
                        continue
                    if board[(box//3)*3+row][(box%3)*3+col] in seen:
                        return False
                    else:
                        seen.add(board[(box//3)*3+row][(box%3)*3+col])
        
        return True
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:        
        def isValid(row, col, ch):
            for i in range(9):
                if board[i][col] == ch:
                    return False

                if board[row][i] == ch:
                    return False
                
                if board[3*(row//3) + i//3][3*(col//3) + i%3] == ch:
                    return False
            
            return True
            
        def solve(row, col):
            if row == 9:
                return True
            if col == 9:
                return solve(row+1, 0)
            
            if board[row][col] == ".":
                for i in range(1, 10):
                    if isValid(row, col, str(i)):
                        board[row][col] = str(i)
                        
                        if solve(row, col + 1):
                            return True
                        else:
                            board[row][col] = "."
                return False
            else:
                return solve(row, col + 1)

        solve(0, 0)
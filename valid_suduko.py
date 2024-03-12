class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_present = [[0]*9 for i in range(9)]
        col_present = [[0]*9 for i in range(9)]
        grid_present = [[0]*9 for i in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val==".":
                    continue
                val = int(val)
                if row_present[row][val-1] == 1:
                    return False
                if col_present[col][val-1] == 1:
                    return False
                if grid_present[row//3 * 3 + col//3][val-1] == 1:
                    return False
                
                row_present[row][val-1]=1
                col_present[col][val-1] = 1
                grid_present[row//3 * 3 + col//3][val-1] = 1


        return True
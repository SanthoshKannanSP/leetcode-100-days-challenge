class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = []
        ans = []
        cols = [False]*n
        diag1 = [False]*(2*n-1)
        diag2 = [False]*(2*n-1)

        def dfs(row,board):
            if row==n:
                ans.append(board)
                return

            for col in range(n):
                if cols[col] or diag1[row+col] or diag2[col-row+n-1]:
                    continue
                cols[col] = diag1[row+col] = diag2[col-row+n-1] = True
                dfs(row+1,board+["."*col + "Q"+ "."*(n-col-1)])
                cols[col] = diag1[row+col] = diag2[col-row+n-1] = False

        dfs(0,[])
        return ans
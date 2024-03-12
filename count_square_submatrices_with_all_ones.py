class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        r,c = len(matrix),len(matrix[0])
        s = 0
        for i in range(r):
            s += matrix[i][0]
        
        for i in range(1,c):
            s += matrix[0][i]

        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][j]==1:
                    matrix[i][j] = min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1]) + 1
                    s += matrix[i][j]

        return s
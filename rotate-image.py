class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        top = 0
        bottom = N - 1

        while top < bottom:
            for col in range(N):
                temp = matrix[top][col]
                matrix[top][col] = matrix[bottom][col]
                matrix[bottom][col] = temp
            top += 1
            bottom -= 1

        for row in range(N):
            for col in range(row+1, N):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
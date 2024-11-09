class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)
        N = len(matrix[0])

        for i in range(M):
            if target<=matrix[i][-1]:
                break

        for j in range(N):
            print(matrix[i][j])
            if target==matrix[i][j]:
                return True
            if target<matrix[i][j]:
                break

        return False
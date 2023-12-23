class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        rowdiff = [0]*m
        coldiff = [0]*n

        for row in range(m):
            for col in range(n):
                if grid[row][col]==1:
                    rowdiff[row]+=1
                    coldiff[col]+=1
                else:
                    rowdiff[row]-=1
                    coldiff[col]-=1

        return [[rowdiff[row]+coldiff[col] for col in range(n)] for row in range(m)]
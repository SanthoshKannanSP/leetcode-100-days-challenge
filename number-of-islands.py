class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row,col,grid):
            grid[row][col]="-"
            
            if row+1<m and grid[row+1][col]=="1":
                grid = dfs(row+1,col,grid)
            if col+1<n and grid[row][col+1]=="1":
                grid = dfs(row,col+1,grid)
            if row-1>=0 and grid[row-1][col]=="1":
                grid = dfs(row-1,col,grid)
            if col-1>=0 and grid[row][col-1]=="1":
                grid = dfs(row,col-1,grid)
            return grid
            
        m = len(grid)
        n = len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    count+=1
                    grid = dfs(i,j,grid)

        return count
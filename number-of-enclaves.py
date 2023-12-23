class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        stack = []

        for i in range(m):
            if grid[i][0]==1:
                stack.append((i,0))
            if grid[i][n-1]==1:
                stack.append((i,n-1))

        for i in range(n):
            if grid[0][i]==1:
                stack.append((0,i))
            if grid[m-1][i]==1:
                stack.append((m-1,i))

        while stack:
            i,j = stack.pop()
            grid[i][j] = -1
            
            if i+1<m and grid[i+1][j]==1:
                stack.append((i+1,j))
            if i-1>=0 and grid[i-1][j]==1:
                stack.append((i-1,j))
            if j+1<n and grid[i][j+1]==1:
                stack.append((i,j+1))
            if j-1>=0 and grid[i][j-1]==1:
                stack.append((i,j-1))
        
        return len([1 for i in range(m) for j in range(n) if grid[i][j]==1])
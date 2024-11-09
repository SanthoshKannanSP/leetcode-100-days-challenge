class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        r,c = len(grid), len(grid[0])
        ans = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j]<0:
                    ans += c-j
                    break

        return ans
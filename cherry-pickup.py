class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def dfs(r1,c1,r2,c2):
            if (r1,c1,r2,c2) in dp:
                return dp[(r1,c1,r2,c2)]

            if r1>=n or c1>=n or r2>=n or c2>=n or grid[r1][c1]==-1 or grid[r2][c2]==-1:
                return -float("inf")

            if r1==c1==n-1:
                return grid[r1][c1]

            curr = 0

            if r1==r2 and c1==c2:
                curr += grid[r1][c1]
            else:
                curr += grid[r1][c1] + grid[r2][c2]

            nxt = -float("inf")
            directions = [(0,1),(1,0)]

            for dx1,dy1 in directions:
                for dx2,dy2 in directions:
                    nxt = max(nxt, dfs(r1+dx1,c1+dy1,r2+dx2,c2+dy2))

            curr += nxt
            dp[(r1,c1,r2,c2)] = curr

            return curr

        n = len(grid)
        dp = dict()
        ans = dfs(0,0,0,0)
        return ans if ans>0 else 0
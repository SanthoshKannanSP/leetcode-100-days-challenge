class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def dfs(r,c1,c2):
            if r==R:
                return 0
            
            if (r,c1,c2) in dp:
                return dp[(r,c1,c2)]
            
            if c1<0 or c1>=n or c2<0 or c2>=n:
                return -float("inf")

            curr = 0
            if c1==c2:
                curr += grid[r][c1]
            else:
                curr += grid[r][c1] + grid[r][c2]

            nxt = -float("inf")
            directions = [-1,0,1]

            for dy1 in directions:
                for dy2 in directions:
                    nxt = max(nxt,dfs(r+1,c1+dy1,c2+dy2))

            curr+=nxt
            dp[(r,c1,c2)] = curr
            return curr

        n = len(grid[0])
        R = len(grid)
        dp = dict()
        ans = dfs(0,0,n-1)

        return ans if ans>0 else 0
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        nodes = [(i, j) for i in range(n) for j in range(m)]
        nm = n*m
        
        def flip(node, grid):
            i, j = node
            for x, y in [(i+1, j), (i, j+1), (i, j), (i-1, j), (i, j-1)]:
                if 0 <= x < n and 0 <= y < m:
                    grid[x][y] ^= 1
       
        ans = float("inf")
        
        for i in range(1 << nm):
            grid = deepcopy(mat) 

            ops = 0
            for j in range(nm):
                if (i >> j) & 1:
                    flip(nodes[j], grid)
                    ops += 1

            if all(sum(grid[i]) == 0 for i in range(n)):
                ans = min(ans, ops)
        
        return ans if ans < float("inf") else -1
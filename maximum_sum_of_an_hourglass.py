class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        hourglass_squares = [(0,0),(0,1),(0,2),(1,1),(2,0),(2,1),(2,2)]
        ROW,COL = len(grid),len(grid[0])
        max_sum = -1

        for row in range(ROW-2):
            for col in range(COL-2):
                curr_sum = 0
                for r,c in hourglass_squares:
                    curr_sum += grid[row+r][col+c]
                max_sum = max(max_sum,curr_sum)

        return max_sum
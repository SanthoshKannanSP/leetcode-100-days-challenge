class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = [point[0] for point in points]
        x.sort()
        return max([x[i]-x[i-1] for i in range(1,len(x))])
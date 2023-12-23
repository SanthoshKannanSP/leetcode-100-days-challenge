class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        x,y = points[0]
        
        count = 0
        for dx,dy in points[1:]:
            count += max(abs(x-dx),abs(y-dy))
            x,y = dx,dy
        
        return count
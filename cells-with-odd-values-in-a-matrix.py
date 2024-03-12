class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row = [0]*m
        col = [0]*n

        for r,c in indices:
            row[r] += 1
            col[c] += 1

        for i in range(m):
            row[i] = row[i]&1==1
        
        for i in range(n):
            col[i] = col[i]&1==1

        count = 0
        for r in range(m):
            for c in range(n):
                if row[r]!=col[c]:
                    count+=1

        return count
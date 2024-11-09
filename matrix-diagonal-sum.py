class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        r = len(mat)
        c = len(mat[0])

        p1,p2 = 0,c-1
        ans = 0

        for i in range(r):
            ans += mat[i][p1]
            if p1!=p2:
                ans += mat[i][p2]
            
            p1+=1
            p2-=1

        return ans
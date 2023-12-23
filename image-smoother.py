class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        m = len(img)
        n = len(img[0])
        ans = [[0]*n for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                s = img[i][j]
                count = 1
                for x,y in directions:
                    if 0<=i+x<m and 0<=j+y<n:
                        s += img[i+x][j+y]
                        count+=1
                ans[i][j] = s//count
        
        return ans
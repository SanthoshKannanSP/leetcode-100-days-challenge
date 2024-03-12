class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        r=len(text2)+1
        c=len(text1)+1
        mat = [[0 for j in range(c)] for i in range(r)]
        for i in range(1,r):
            for j in range(1,c):
                if text2[i-1]==text1[j-1]:
                    mat[i][j]=mat[i-1][j-1]+1
                else:
                    mat[i][j]=max(mat[i-1][j],mat[i][j-1])
        return mat[-1][-1]
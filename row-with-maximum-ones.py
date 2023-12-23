class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        row = 0
        count = 0

        for i in range(len(mat)):
            m = mat[i].count(1)
            if m>count:
                count = m
                row = i

        return [row,count]
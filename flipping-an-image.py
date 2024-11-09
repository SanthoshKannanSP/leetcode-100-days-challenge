class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rev = [i[::-1] for i in image]

        return [[0 if i==1 else 1 for i in j] for j in rev]
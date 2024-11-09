class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        s1 = set()
        s2 = set()
        n = len(A)
        ans = []

        for i in range(n):
            s1.add(A[i])
            s2.add(B[i])
            ans.append(len(s1.intersection(s2)))

        return ans
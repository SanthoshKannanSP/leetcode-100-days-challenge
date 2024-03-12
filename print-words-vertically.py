class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        n = max(len(i) for i in words)
        ans = [""] * n

        for i in words:
            for j in range(len(i)):
                ans[j] += i[j]
            j += 1
            while j < n:
                ans[j] += " "
                j += 1

        return [i.rstrip() for i in ans]

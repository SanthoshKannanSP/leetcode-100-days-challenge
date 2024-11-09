class Solution:
    def minimizedStringLength(self, s: str) -> int:
        n = set([i for i in s])

        return len(n)
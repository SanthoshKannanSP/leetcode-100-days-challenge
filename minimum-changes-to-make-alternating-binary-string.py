class Solution:
    def minOperations(self, s: str) -> int:
        zero = 0
        n = len(s)

        for i in range(n):
            if i % 2 == 0:
                if s[i] == "1":
                    zero += 1
            else:
                if s[i] == "0":
                    zero += 1

        return min(zero, n - zero)

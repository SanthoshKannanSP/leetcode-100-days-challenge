class Solution:
    def appealSum(self, s: str) -> int:
        last_occur = {}
        ans = 0
        n = len(s)

        for i in range(n):
            char = s[i]
            last_occur[char] = i+1
            ans += sum(last_occur.values())

        return ans
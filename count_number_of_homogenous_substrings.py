class Solution:
    def countHomogenous(self, s: str) -> int:
        count = 0
        n = len(s)
        streak = 0
        mod = 10**9 + 7

        for i in range(n):
            if i==0 or s[i]==s[i-1]:
                streak+=1
            else:
                streak=1
            count = (count+streak)%mod

        return count
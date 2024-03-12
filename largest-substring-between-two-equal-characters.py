class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = defaultdict(int)
        ans = -1

        for i,ch in enumerate(s):
            if ch in d:
                ans = max(ans,i-d[ch]-1)
            else:
                d[ch]=i

        return ans
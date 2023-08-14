class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq_s = Counter(s)
        freq_t = Counter(t)

        for char in freq_t:
            if freq_t[char]!=freq_s[char]:
                return char
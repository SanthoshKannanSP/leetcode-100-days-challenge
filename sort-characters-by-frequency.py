class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        return "".join(sorted(s, reverse=True, key=lambda x: (freq[x], x)))

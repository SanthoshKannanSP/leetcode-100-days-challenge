class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        ans = ""

        for char in order:
            if char in freq:
                ans += char*freq[char]
                freq[char]=0
        
        for char in freq:
            ans += char*freq[char]

        return ans
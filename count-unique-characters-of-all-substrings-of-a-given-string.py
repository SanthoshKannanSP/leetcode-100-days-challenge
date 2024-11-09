class Solution:
    def uniqueLetterString(self, s: str) -> int:
        occurs = {c: [-1, -1] for c in ascii_uppercase}
        ans = 0
        n = len(s)

        for k in range(n):
            char = s[k]
            i, j = occurs[char]
            ans += (j - i) * (k - j)
            occurs[char] = [j, k]

        for char in occurs:
            j, k = occurs[char]
            ans += (k-j)*(n-k)

        return ans
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        word_counts = [Counter(word) for word in words]

        ans = 0
        n = len(words)

        for i in range(n):
            for char in word_counts[i]:
                if chars_count[char]<word_counts[i][char]:
                    break
            else:
                ans += len(words[i])

        return ans
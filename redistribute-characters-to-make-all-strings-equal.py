class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = defaultdict(int)
        n = len(words)

        for word in words:
            for char in word:
                freq[char] += 1

        return all(i%n==0 for i in freq.values())
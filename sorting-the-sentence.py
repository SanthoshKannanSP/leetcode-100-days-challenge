class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        ans = [""]*len(words)

        for word in words:
            pos = int(word[-1])
            ans[pos-1] = word[:-1]

        return " ".join(ans)
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def convert(word):
            value = 0
            d = dict()
            for i in word:
                if i in d:
                    continue
                else:
                    d[i] = value
                    value+=1
            return [d[i] for i in word]

        pattern = convert(pattern)
        ans = []
        for word in words:
            if convert(word)==pattern:
                ans.append(word)

        return ans
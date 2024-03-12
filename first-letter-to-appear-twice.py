class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = dict()

        for i in s:
            if i in d:
                return i
            d[i] = 1

        return i
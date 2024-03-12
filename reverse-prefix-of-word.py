class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        temp = ""
        changed = False

        for char in word:
            temp+=char
            if char==ch and not changed:
                temp = temp[::-1]
                changed = True

        return temp

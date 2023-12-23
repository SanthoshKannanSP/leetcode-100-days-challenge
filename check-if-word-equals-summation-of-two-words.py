class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        n1 = "".join([f"{ord(i)-97}" for i in firstWord])
        n2 = "".join([f"{ord(i)-97}" for i in secondWord])

        n = "".join([f"{ord(i)-97}" for i in targetWord])

        return int(n1)+int(n2)==int(n)
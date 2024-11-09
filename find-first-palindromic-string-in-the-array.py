class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(s):
            if s==s[::-1]:
                return True


        for word in words:
            if isPalindrome(word):
                return word

        return ""
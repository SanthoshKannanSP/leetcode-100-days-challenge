class Solution:
    def sortVowels(self, s: str) -> str:
        sorted_vowels = sorted([vowel for vowel in s if vowel.lower() in "aeiou"],reverse=True)

        return "".join([sorted_vowels.pop() if letter.lower() in "aeiou" else letter for letter in s ])
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_freq = Counter(ransomNote)
        magazine_freq = Counter(magazine)

        for i in ransom_freq:
            if i not in magazine:
                return False
            if ransom_freq[i] > magazine_freq[i]:
                return False
        
        return True
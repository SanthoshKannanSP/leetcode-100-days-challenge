class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = set([i for i in allowed])
        count = 0

        for word in words:
            for char in word:
                if char not in c:
                    break
            else:
                count+=1
        
        return count
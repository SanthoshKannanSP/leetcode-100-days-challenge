class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = dict()
        mapped = set()
        words = s.split()

        n = len(pattern)

        if n != len(words):
            return False

        i = 0

        while i < n:
            if pattern[i] not in mapping:
                if words[i] in mapped:
                    return False
                mapping[pattern[i]] = words[i]
                mapped.add(words[i])
            elif mapping[pattern[i]] != words[i]:
                return False
            i += 1
        
        return True
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = dict()
        
        if len(s)!=len(t):
            return False
        
        n = len(s)
        i = 0
        mapped = set()

        while i<n:
            if t[i] not in mapping:
                if s[i] in mapped:
                    return False
                mapping[t[i]] = s[i]
                mapped.add(s[i])
            elif mapping[t[i]] != s[i]:
                return False
            i+=1

        return True
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        n = len(s)
        if n==1:
            return False
        present = set()
        rev = s[::-1]
        
        for i in range(0,n-1,1):
            present.add(s[i]+s[i+1])
            
        for i in range(0,n-1,1):
            if rev[i]+rev[i+1] in present:
                return True
            
        return False
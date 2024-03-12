class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        ns = len(s)
        na = len(a)
        nb = len(b)
        
        ai = []
        bi = []
        
        for i in range(ns-na+1):
            if s[i:i+na]==a:
                ai.append(i)
                
        for i in range(ns-nb+1):
            if s[i:i+nb]==b:
                bi.append(i)
        
        ans = []
        for i in ai:
            for j in bi:
                if abs(i-j)<=k:
                    ans.append(i)
                    break
                    
        return sorted(ans)
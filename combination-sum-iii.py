class Solution:
    ans = []
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        def dfs(val,s,comb):
            if s>n:
                return
            if val>9:
                return
            if len(comb)>k:
                return

            if s+val==n and len(comb)+1==k:
                comb.append(val)
                self.ans.append(comb.copy())
                comb.pop()
                return
            
            dfs(val+1,s,comb)
            comb.append(val)
            dfs(val+1,s+val,comb)
            comb.pop()
            return

        dfs(1,0,[])
        return self.ans
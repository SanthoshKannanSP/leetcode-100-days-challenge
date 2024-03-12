class Solution:
    ans = []
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        def dfs(i,comb):
            if len(comb)==k:
                self.ans.append(comb[:])
                return
            if i>n:
                return
            
            comb.append(i)
            dfs(i+1,comb)
            comb.pop()
            dfs(i+1,comb)
            return

        dfs(1,[])
        return self.ans
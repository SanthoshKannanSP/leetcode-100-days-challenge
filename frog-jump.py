class Solution:
    def canCross(self, stones: List[int]) -> bool:
        @lru_cache(None)
        def dfs(position,step):
            if position not in stones:
                return False
            if position == stones[-1]:
                return True
            if step==0:
                return False
            return dfs(position+step+1,step+1) or dfs(position+step,step) or dfs(position+step-1,step-1)

        if stones[1]!=1:
            return False
        return dfs(1,1)
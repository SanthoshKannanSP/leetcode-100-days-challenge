class Solution:
    ans = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.ans = []
        
        def dfs(stack,rem):
            if not rem:
                self.ans.append(stack[:])
            
            for i in range(len(rem)):
                stack.append(rem.pop(0))
                dfs(stack,rem)
                rem.append(stack.pop())

            return
        
        dfs([],nums)
        return self.ans
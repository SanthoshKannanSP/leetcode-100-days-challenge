class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        
        def search(stack,index,target):
            if target==0:
                ans.append(stack[:])
                return
            if index >= n:
                return
            if candidates[index] <= target:
                stack.append(candidates[index])
                search(stack,index,target-candidates[index])
                stack.pop()
            search(stack,index+1,target)
            return

        search([],0,target)

        return ans
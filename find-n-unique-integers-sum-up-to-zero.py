class Solution:
    def sumZero(self, n: int) -> List[int]:
        val = 1
        ans = []

        for i in range(0,n-1,2):
            ans.append(val)
            ans.append(-val)
            val+=1
        
        if n&1==1:
            ans.append(0)
        
        return ans
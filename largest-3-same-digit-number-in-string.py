class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        if n<3:
            return ""
        
        ans = ""

        for i in range(2,n):
            if num[i]==num[i-1] and num[i]==num[i-2]:
                ans = max(num[i-2:i+1],ans)

        return ans
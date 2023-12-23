class Solution:
    def numberOfSteps(self, num: int) -> int:
        b = bin(num).replace("0b","")
        ans = 0
        for i in b:
            if i=="1":
                ans+=2
            else:
                ans+=1
        return ans-1
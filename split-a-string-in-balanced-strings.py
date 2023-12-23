class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        right = 0
        left = 0

        for i in s:
            if i=="R":
                right+=1
            else:
                left+=1
            if right==left:
                count+=1
                right=0
                left=0

        return count
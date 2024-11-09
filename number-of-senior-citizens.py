class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for det in details:
            if int(det[11:13])>60:
                ans+=1

        return ans
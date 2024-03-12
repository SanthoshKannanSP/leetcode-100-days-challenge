class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        start = 0
        end = len(s)

        ans = []

        for i in s:
            if i=="I":
                ans.append(start)
                start+=1
            else:
                ans.append(end)
                end-=1
        
        ans.append(start)
        return ans
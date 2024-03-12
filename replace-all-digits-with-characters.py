class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ""
        
        for i in s:
            if i.isdigit():
                ans += chr(ord(ans[-1])+int(i))
            else:
                ans += i

        return ans
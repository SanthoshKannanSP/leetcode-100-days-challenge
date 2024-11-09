class Solution:
    def calculate(self, s: str) -> int:
        ans = 0
        num = 0
        sign = 1
        stack = []

        for i in s:
            if i.isdigit():
                num = (num*10)+int(i)
            elif i in "-+":
                ans += num*sign
                sign = -1 if i=="-" else 1
                num = 0
            elif i=="(":
                stack.append(ans)
                stack.append(sign)
                ans = 0
                sign = 1
            elif i==")":
                ans += sign*num
                ans *= stack.pop()
                ans += stack.pop()
                num = 0

        return ans+num*sign
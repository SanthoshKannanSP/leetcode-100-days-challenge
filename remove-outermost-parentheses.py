class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ans = ""
        op,cl = 0,0

        for i in s:
            stack.append(i)
            if i=="(":
                op+=1
            else:
                cl+=1
            
            if op==cl:
                ans += "".join(stack[1:-1])
                stack = []
                op=0
                cl=0

        return ans
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0

        for i in s:
            if i==")":
                if not stack:
                    count+=1
                else:
                    stack.pop()
            else:
                stack.append(i)

        return count+len(stack)
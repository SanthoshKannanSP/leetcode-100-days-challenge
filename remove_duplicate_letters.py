class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {s[i]:i for i in range(len(s))}
        stack = []

        for i in range(len(s)):
            if s[i] in stack:
                continue
            elif not stack:
                stack.append(s[i])
            else:
                while stack and stack[-1]>s[i] and last[stack[-1]]>i:
                    stack.pop()
                stack.append(s[i])

        return "".join(stack)
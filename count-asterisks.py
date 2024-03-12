class Solution:
    def countAsterisks(self, s: str) -> int:
        stack = []
        count = 0

        for i in s:
            if i=="|":
                if not stack:
                    stack.append(i)
                else:
                    stack.pop()

            elif i=="*" and not stack:
                count+=1

        return count
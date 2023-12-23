class Solution:
    def maximum69Number (self, num: int) -> int:
        n = str(num)
        ans = ""
        changed = False

        for i in n:
            if i=="6" and not changed:
                ans += "9"
                changed = True
            else:
                ans += i

        return int(ans)
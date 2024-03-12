class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        t_pointer = 0
        s_len = len(s)
        t_len = len(t)

        if s_len == 0:
            return True

        if t_len == 0:
            return False

        while t_pointer < t_len:
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
                if s_pointer >= s_len:
                    return True
            t_pointer += 1

        return False
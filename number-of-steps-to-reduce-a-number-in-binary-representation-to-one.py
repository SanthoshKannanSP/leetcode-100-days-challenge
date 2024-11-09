class Solution:
    def numSteps(self, s: str) -> int:
        s = list(s)

        def add_1(string):
            i = -1
            string = ["0"] + string
            while string[i] == "1":
                string[i] = "0"
                i -= 1
            string[i] = "1"
            for i in range(len(string)):
                if string[i] == "1":
                    break
            return string[i:]

        count = 0
        while len(s) > 1:
            if s[-1] == "1":
                s = add_1(s)
            else:
                s.pop()
            count += 1
        return count

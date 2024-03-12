class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy,yx = 0,0

        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                if s1[i]=="x":
                    xy += 1
                else:
                    yx += 1

        print(xy,yx)
        if (xy+yx) %2 ==1:
            return -1

        res = xy + yx

        if xy%2==1:
            res+=2
        return res//2
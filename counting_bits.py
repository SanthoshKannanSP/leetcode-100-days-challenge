class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0,1]
        if n<2:
            return res[:n+1]

        for i in range(2,n+1):
            if i%2==0:
                res.append(res[i//2])
            else:
                res.append(1+res[i//2])

        return res
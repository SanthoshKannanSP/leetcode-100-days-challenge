class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left,right+1):
            digits = set([int(j) for j in str(i)])
            for digit in digits:
                if digit==0 or i%digit!=0:
                    break
            else:
                ans.append(i)

        return ans
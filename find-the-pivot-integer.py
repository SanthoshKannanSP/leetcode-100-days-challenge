class Solution:
    def pivotInteger(self, n: int) -> int:
        start = 1
        end = n

        def sumTillN(n):
            return (n*(n+1))//2

        total = sumTillN(n)

        while start<=end:
            mid = start + (end-start)//2
            left = sumTillN(mid)
            if left==total-left+mid:
                return mid
            elif left<total-left:
                start = mid+1
            else:
                end = mid-1

        return -1
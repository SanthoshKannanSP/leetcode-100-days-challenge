class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_carry(capacity):
            d = 1
            total = 0
            for weight in weights:
                total += weight
                if total>capacity:
                    total = weight
                    d+=1
                    if d>days:
                        return False
            return True

        left = max(weights)
        right = sum(weights)

        while left<right:
            mid = left + (right-left)//2
            if can_carry(mid):
                right = mid
            else:
                left = mid + 1
        return left
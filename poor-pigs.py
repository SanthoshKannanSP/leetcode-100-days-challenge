class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return math.ceil(round(math.log(buckets, minutesToTest // minutesToDie + 1), 10))
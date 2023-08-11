class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = collections.defaultdict(int)
        pairs = 0

        for num in nums:
            pairs += count[num]
            count[num] += 1


        return pairs
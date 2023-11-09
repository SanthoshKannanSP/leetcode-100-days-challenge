class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        freq = sorted(freq,key=lambda x: freq[x])
        return freq[-k:]
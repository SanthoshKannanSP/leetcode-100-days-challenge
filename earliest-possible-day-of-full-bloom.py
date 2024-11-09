class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        last_plant_day = 0
        max_bloom_day = -float('inf')
        times = sorted(zip(growTime, plantTime), reverse=True)

        for gtime, ptime in times:
            max_bloom_day = max(max_bloom_day, last_plant_day + ptime + gtime)
            last_plant_day += ptime
        
        return max_bloom_day
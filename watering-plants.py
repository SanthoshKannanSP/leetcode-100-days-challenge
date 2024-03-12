class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        can = capacity
        n = len(plants)
        count = 0
        
        for i in range(n):
            if can<plants[i]:
                count += 2*i
                can = capacity
            count += 1
            can -= plants[i]

        return count
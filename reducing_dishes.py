class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        curr_sat = satisfaction.pop()
        max_sat = 0

        while curr_sat >= 0:
            max_sat += curr_sat
            if not satisfaction:
                break
            curr_sat += satisfaction.pop()
        
        return max_sat
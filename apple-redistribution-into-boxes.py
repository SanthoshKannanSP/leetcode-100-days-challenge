class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s = sum(apple)
        capacity.sort(reverse=True)
        
        for i in range(len(capacity)):
            s-=capacity[i]
            if s<=0:
                return i+1
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        indices = [i for i in range(n)]

        indices.sort(key=lambda x: heights[x],reverse=True)

        return [names[i] for i in indices]
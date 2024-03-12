class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        n = len(colors)
        curr = neededTime[0]
        m = neededTime[0]

        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                curr += neededTime[i]
                m = max(neededTime[i], m)
            else:
                ans += curr - m
                curr = neededTime[i]
                m = neededTime[i]

        if colors[-1] == colors[-2]:
            ans += curr - m

        return ans

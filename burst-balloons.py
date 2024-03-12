class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = defaultdict(int)

        def dfs(start,end):
            if start>end:
                return 0

            if start==end:
                s = nums[start]
                if start-1>=0:
                    s*=nums[start-1]
                if end+1<n:
                    s*=nums[end+1]
                return s

            if (start,end) not in dp:
                ans = 0
                for i in range(start,end+1):
                    s = nums[i]
                    if start-1>=0:
                        s*=nums[start-1]
                    if end+1<n:
                        s*=nums[end+1]
                    
                    left = dfs(start,i-1)
                    right = dfs(i+1,end)
                    ans = max(ans,s+left+right)

                dp[(start,end)] = ans

            return dp[(start,end)]

        nums.insert(0,1)
        nums.append(1)
        n = len(nums)
        p = dfs(1,n-2)
        print(dp)
        return p
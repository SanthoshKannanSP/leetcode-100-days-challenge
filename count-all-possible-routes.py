class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9 + 7
        n = len(locations)
        dp = [[-1]*(fuel+1) for i in range(n)]

        def dfs(current,destination,fuel):
            if fuel<0:
                return 0
            
            if dp[current][fuel]==-1:
                count = 1 if current==destination else 0

                for city in range(n):
                    if city!=current and fuel>=abs(locations[city]-locations[current]):
                        count += dfs(city,destination,fuel-abs(locations[city]-locations[current]))
                        count%=MOD

                dp[current][fuel] = count
            
            return dp[current][fuel]

        return dfs(start,finish,fuel)
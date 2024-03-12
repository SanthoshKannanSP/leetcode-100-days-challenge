class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = defaultdict(int)
        MOD = (10**9) + 7

        def rolls(dice, target):
            if dice == 0:
                return 0 if target > 0 else 1
            if (dice, target) not in dp:
                ways = 0
                for i in range(max(0, target - k), target):
                    ways += rolls(dice - 1, i)
                dp[(dice, target)] = ways

            return dp[(dice, target)]

        return rolls(n, target) % MOD

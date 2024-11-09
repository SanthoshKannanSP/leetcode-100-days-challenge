class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        dungeon[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])

        for i in range(m - 2, -1, -1):
            dungeon[i][n - 1] = max(1, dungeon[i + 1][n - 1] - dungeon[i][n - 1])

        for i in range(n - 2, -1, -1):
            dungeon[m - 1][i] = max(1, dungeon[m - 1][i + 1] - dungeon[m - 1][i])

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                s = min(dungeon[i + 1][j], dungeon[i][j + 1])
                dungeon[i][j] = max(1, s - dungeon[i][j])

        return dungeon[0][0]

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldier_count = defaultdict(list)

        for i in range(len(mat)):
            count = mat[i].count(1)
            soldier_count[count].append(i)

        ans = []
        i = 0
        for count in sorted(soldier_count):
            for row in soldier_count[count]:
                ans.append(row)
                i+=1
                if i==k:
                    return ans

        return ans
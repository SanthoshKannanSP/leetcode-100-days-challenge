class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        ans = 0
        for row in bank:
            curr = row.count("1")
            if curr==0:
                continue
            ans += curr*prev
            prev = curr

        return ans
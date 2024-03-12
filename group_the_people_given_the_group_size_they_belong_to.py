class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups_count = collections.defaultdict(list)
        
        for i in range(len(groupSizes)):
            groups_count[groupSizes[i]].append(i)

        ans = []

        for i in groups_count:
            for j in range(0,len(groups_count[i]),i):
                ans.append(groups_count[i][j:j+i])
        return ans
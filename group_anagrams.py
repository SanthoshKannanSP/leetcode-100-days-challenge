class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        s_strs = ["".join(sorted(i)) for i in strs]

        ans = defaultdict(list)

        for i in range(len(strs)):
            ans[s_strs[i]].append(strs[i])
        
        return ans.values()
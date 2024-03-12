class Solution:
    dp = defaultdict(int)
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def solve(start,end):
            if start>end:
                return [None]
            if start==end:
                return [TreeNode(start)]
            if (start,end) not in self.dp:
                ans = []
                for i in range(start,end+1):
                    left = solve(start,i-1)
                    right = solve(i+1,end)
                    for l in left:
                        for r in right:
                            root = TreeNode(i)
                            root.left = l
                            root.right = r
                            ans.append(root)
                self.dp[(start,end)] = ans
            
            return self.dp[(start,end)]

        return solve(1,n)
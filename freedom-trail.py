class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        N = len(ring)
        dp = defaultdict(int)

        def dfs(ring_index,key_index):
            if key_index==len(key):
                return 0
            
            if (ring_index,key_index) not in dp:
                ans = float("inf")
                for k,c in enumerate(ring):
                    if c==key[key_index]:
                        dist = min(abs(k-ring_index),N-abs(k-ring_index))
                        ans = min(ans,1+dist+dfs(k,key_index+1))
                
                dp[(ring_index,key_index)] = ans
            
            return dp[(ring_index,key_index)]

        return dfs(0,0)
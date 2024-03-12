class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        prefix_sum = [0]

        balls = 0
        for i in range(n):
            balls += int(boxes[i])
            prefix_sum.append(prefix_sum[-1]+balls)

        suffix_sum = [0]
        balls = 0
        for i in range(n-1,-1,-1):
            balls += int(boxes[i])
            suffix_sum.append(suffix_sum[-1]+balls)
        
        suffix_sum = suffix_sum[::-1]
        res = []
        for i in range(n):
            res.append(prefix_sum[i]+suffix_sum[i+1])

        return res
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = [0]*26
        
        for char in s:
            freq[ord(char)-97] += 1

        for char in t:
            freq[ord(char)-97] -= 1

        pos_sum = sum([i for i in freq if i>0])
        neg_sum = sum([-i for i in freq if i<0])

        return min(pos_sum,neg_sum)
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        mscore = 0

        while tokens:
            if tokens[0]<=power:
                t = tokens.pop(0)
                power -= t
                score += 1
                mscore = max(mscore,score)
            elif score>0:
                t = tokens.pop()
                power += t
                score -= 1
            else:
                break
        
        return mscore
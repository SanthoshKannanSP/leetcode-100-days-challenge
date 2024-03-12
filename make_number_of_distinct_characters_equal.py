class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        freq1, freq2 = Counter(word1),Counter(word2)

        for c1 in string.ascii_lowercase:
            for c2 in string.ascii_lowercase:

                if c1 not in freq1 or c2 not in freq2:
                    continue
                
                freq1[c2] += 1
                freq1[c1] -= 1

                if freq1[c1]==0:
                    del freq1[c1]

                freq2[c1] += 1
                freq2[c2] -= 1

                if freq2[c2]==0:
                    del freq2[c2]

                if len(freq1)==len(freq2):
                    return True

                freq1[c2] -= 1
                freq1[c1] += 1

                if freq1[c2]==0:
                    del freq1[c2]

                freq2[c1] -= 1
                freq2[c2] += 1

                if freq2[c1]==0:
                    del freq2[c1]
                
        return False
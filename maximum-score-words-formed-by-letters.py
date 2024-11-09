class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        self.ans = 0
        n = len(words)
        freq = Counter(letters)

        def dfs(index,currScore):
            self.ans = max(self.ans,currScore)
            if index==n:
                return

            wordScore = 0
            for letter in words[index]:
                wordScore += score[ord(letter)-97]
                freq[letter]-=1

            if min(freq.values())>=0:
                dfs(index+1,currScore+wordScore)
            
            for letter in words[index]:
                freq[letter]+=1

            dfs(index+1,currScore)
            return

        dfs(0,0)
            
        return self.ans
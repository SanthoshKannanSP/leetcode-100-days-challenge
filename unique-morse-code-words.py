class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        chars = string.ascii_lowercase

        d = dict(zip(chars,morse))
        
        s = set()

        for word in words:
            a = ""
            for c in word:
                a += d[c]
            s.add(a)

        return len(s)
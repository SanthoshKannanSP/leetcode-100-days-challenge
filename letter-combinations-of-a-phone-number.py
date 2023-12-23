class Solution:
    letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        if len(digits)==1:
            return [i for i in self.letters[digits]]
            return
        
        ans = []
        combs = self.letterCombinations(digits[1:])
        for letter in self.letters[digits[0]]:
            for comb in combs:
                ans.append(letter+comb)

        return ans
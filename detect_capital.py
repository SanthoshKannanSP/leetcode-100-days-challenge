class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        all_caps = False
        first_caps = False

        if word[0].isupper():
            first_caps = True

        n = len(word)

        for i in range(1,n):
            if i==1 and first_caps:
                if word[i].isupper():
                    all_caps = True
            else:
                if word[i].isupper():
                    if all_caps:
                        continue
                    return False
                else:
                    if all_caps:
                        return False
        
        return True
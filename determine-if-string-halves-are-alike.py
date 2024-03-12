class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        left,right=0,len(s)-1
        c = 0

        while left<right:
            if s[left] in vowels:
                c+=1
            if s[right] in vowels:
                c-=1
            left+=1
            right-=1

        if c==0:
            return True
        return False
class Solution:
    def reverseVowels(self, s: str) -> str:
        ans = list(s)
        left = 0
        right = len(s)-1
        vowels = "aeiouAEIOU"

        while(left<right):
            if s[left] in vowels and s[right] in vowels:
                ans[left], ans[right] = s[right],s[left]
            elif s[left] in vowels:
                right -= 1
                continue
            elif s[right] in vowels:
                left += 1
                continue
            left += 1
            right -= 1
        
        return "".join(ans)
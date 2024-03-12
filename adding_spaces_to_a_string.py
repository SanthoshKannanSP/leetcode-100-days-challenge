class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        spaces_pointer = 0

        for i in range(len(s)):
            if spaces_pointer<len(spaces) and i==spaces[spaces_pointer]:
                ans += " "
                spaces_pointer+=1
            ans += s[i]

        return ans
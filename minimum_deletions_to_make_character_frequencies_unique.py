class Solution:
    def minDeletions(self, s: str) -> int:
        char_array = [0]*26
        print(ord("a"))
        for i in s:
            char_array[ord(i)-97] += 1
        
        count = 0
        for i in range(26):
            value = char_array.pop(0)
            while value in char_array and value!=0:
                value-=1
                count+=1
            char_array.append(value)

        return count
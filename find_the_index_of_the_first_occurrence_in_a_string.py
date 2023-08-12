class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_length = len(needle)
        haystack_length = len(haystack)

        if needle_length > haystack_length:
            return -1

        window_end = needle_length - 1

        window = " "

        for i in range(window_end):
            window += haystack[i]

        while window_end<haystack_length:
            window = window[1:] + haystack[window_end]
            if window == needle:
                return window_end - needle_length + 1
            window_end += 1
            
        return -1
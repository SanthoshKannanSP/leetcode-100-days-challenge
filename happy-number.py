class Solution:
    def isHappy(self, n: int) -> bool:
        def digitSum(n):
            s = 0
            while n:
                rem = n%10
                s += rem**2
                n //= 10
            return s
        
        slow = n
        fast = n

        slow = digitSum(slow)
        fast = digitSum(digitSum(fast))

        while slow!=fast:
            slow = digitSum(slow)
            fast = digitSum(digitSum(fast))
        if slow == 1:
            return 1
        else:
            return 0
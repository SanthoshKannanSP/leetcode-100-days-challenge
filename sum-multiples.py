class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def ap_sum(num,count):
            return (num*(count)*(count+1))//2

        return ap_sum(3,n//3)+ap_sum(5,n//5)+ap_sum(7,n//7)-ap_sum(15,n//15)-ap_sum(21,n//21)-ap_sum(35,n//35)+ap_sum(105,n//105)
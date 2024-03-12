class Solution:
    def totalMoney(self, n: int) -> int:
      weeks = n//7
      rem = n%7
      F = 28
      L = 28 + (weeks-1) * 7
      
      asum = weeks*(F+L)//2
      fsum = 0
      for i in range(rem):
        fsum+=weeks+1+i

      return asum+fsum
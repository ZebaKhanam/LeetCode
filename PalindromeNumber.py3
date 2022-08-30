import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x == 0):
            return True
        if(x>0):
          l = math.floor(math.log10(x)+1)  
          if(l == 1):
            return True
          for m in range(l//2):
                if(((x//(10**m))%10)!=((x//(10**(l-m-1)))%10)):
                    return False
          return True

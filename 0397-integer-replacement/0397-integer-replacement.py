class Solution:
    def integerReplacement(self, n: int) -> int:
        x=0
        while n!=1:
            x+=1
            if n%2==0:
                n//=2
            elif n%4==1 or n<4 :
                n=n-1
            else:
                n+=1
      
        return x


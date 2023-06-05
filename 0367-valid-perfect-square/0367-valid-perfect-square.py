class Solution:
    def isPerfectSquare(self, a: int) -> bool:
        n=20
        x=10
        y=0.5*(x+a/x)
        for i in range(n):
            y=0.5*(y+a/y)
        if (y%1==0):
            return True
        else:
            return False
        


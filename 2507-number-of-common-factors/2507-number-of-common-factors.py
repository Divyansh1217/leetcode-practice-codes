class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        c=min(a,b)
        d=0
        for i in range(1,c+1):
            if a%i==0 and b%i==0:
                d=d+1
        return d

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        s,t=0,0
        for i in range(1,n+1):
            if i%m==0:
                s=s+i
            else:
                t=t+i
        return t-s

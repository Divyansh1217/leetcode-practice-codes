class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cr=[1]*n
        pr=[1]*n
        for i in range(1,m):
            for j in range(1,n):
                cr[j]=cr[j-1]+pr[j]
            cr,pr=pr,cr
        return pr[-1]
class Solution:
    def numberOfMatches(self, n: int) -> int:
        a=0
        while n!=1:
            if n%2==0:
                c=n/2
                n=n-c
                a=a+c
            else:
                c=(n-1)/2
                n=n-c
                a=a+c
        return int(a)
            

        
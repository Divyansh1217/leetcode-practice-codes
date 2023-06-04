class Solution:
    def addDigits(self, a: int) -> int:
        if(a<10):
            return a
        
        while(a>9):
            b=0

            n = str(a)
            n = map(int, n)
            n=list(n)
            for i in range(len(n)):
                b=b+n[i]
            a=b
        return a    

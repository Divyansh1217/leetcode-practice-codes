class Solution:
    def countDigits(self, num: int) -> int:
        a=list(map(int,str(num)))
        b=0
        for i in range(len(a)):
            if (num%a[i]==0):
                b=b+1
            else:
                continue
        return b

        
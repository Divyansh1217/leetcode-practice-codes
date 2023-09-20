class Solution:
    def numberOfSteps(self, num: int) -> int:
        a=0
        b=num
        while b!=0:
            if b%2==0:
                b=b/2
                a=a+1
            else:
                b=b-1
                a=a+1
        return a


        
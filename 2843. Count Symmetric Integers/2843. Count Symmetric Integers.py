class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for i in range(low,high+1):
            lenNum=len(str(i))
            if lenNum%2==0:
                smf=0
                sms=0
                for j in str(i)[:lenNum//2]:
                    smf+=int(j)
                for k in str(i)[lenNum//2:]:
                    sms+=int(k)
                if smf==sms:
                    count+=1
        return count               

        

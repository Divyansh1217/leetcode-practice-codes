class Solution:
    def convertTemperature(self, c: float) -> List[float]:
        a=[]
        k=c+273.15
        f=c*1.80+32.00
        a.append(k)
        a.append(f)
        return a
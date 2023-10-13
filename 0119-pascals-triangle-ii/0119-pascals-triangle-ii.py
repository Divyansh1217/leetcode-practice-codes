class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        p=1
        a=[]
        a.append(1)
        for i in range(1,rowIndex+1):
            c=p*(rowIndex-i+1)//i
            a.append(c)
            p=c
        return a
            
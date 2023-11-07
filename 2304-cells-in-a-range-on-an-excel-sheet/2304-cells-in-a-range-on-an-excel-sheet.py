class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        k,k1,l=int(s[1]),int(s[4]),[]
        for i in range(ord(s[0]),ord(s[3])+1):
            for j in range(int(s[1]),int(s[4])+1):
                l1=''
                l1+=chr(i)
                l1+=str(j)
                l.append(l1)
        return l
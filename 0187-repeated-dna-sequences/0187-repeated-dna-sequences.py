class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l=set()
        p=set()
        n=len(s)
        if n<=10:
            return list(l)
        for i in range(0,n-9):
            st=s[i:i+10]
            if st in l and st not in p:
                p.add(st)
            elif st not in l:
                l.add(st)
        return list(p)
        
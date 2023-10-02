class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        n=[]
        for i in set(s):
            n.append(s.count(i))
        if len(set(n))==1:
            return True
        return False

        
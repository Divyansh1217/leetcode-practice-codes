class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        a=[]
        a.append(pref[0])
        i=0
        j=1
        while i< len(pref)-1 and j<=len(pref)-1:
            b=pref[i]^pref[j]
            a.append(b)
            i=i+1
            j=j+1
        return a
        
            



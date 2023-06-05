class Solution:
    def intersection(self, n1: List[int], n2: List[int]) -> List[int]:
        n3=[]
        n1=set(n1)
        n2=set(n2)
        n1=list(n1)
        n2=list(n2)
        for i in range(len(n1)):
            for j in range(len(n2)):
                if (n1[i]==n2[j]):
                    n3.append(n1[i])
                else:
                    continue
        return(n3)
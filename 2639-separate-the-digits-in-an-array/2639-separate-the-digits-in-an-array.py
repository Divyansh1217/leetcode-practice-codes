class Solution:
    def separateDigits(self, n: List[int]) -> List[int]:
        a=[]
        for i in range(len(n)):
            b=list(map(int,str(n[i])))
            a=a+b
        return a
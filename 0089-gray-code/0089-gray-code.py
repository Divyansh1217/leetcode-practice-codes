class Solution:
    def grayCode(self, n: int) -> List[int]:
        a=2**n
        b=[]
        for i in range(a):
            res=i^(i//2)
            b.append(res)
        return b
        
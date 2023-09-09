class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a=[(b:=[1])]
        for i in range(1,numRows):
            b=list(map(sum,pairwise([0]+b+[0])))
            a.append(b)
        return a
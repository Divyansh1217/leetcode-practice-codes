import math
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n=list(map(int,str(n)))
        b=math.prod(n)
        c=sum(n)
        return (b-c)
        
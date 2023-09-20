from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        a=[]
        for i in range(1,n+1):
            a.append(i)
        b=list(permutations(a))
        return ''.join(map(str,b[k-1]))

        
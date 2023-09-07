class Solution:
    def maxSubArray(self, a: List[int]) -> int:
        maxi,b=float('-inf'),0
        for i in range(len(a)):
            b=b+a[i]
            maxi=max(maxi,b)
            b=max(b,0)
        return maxi
        



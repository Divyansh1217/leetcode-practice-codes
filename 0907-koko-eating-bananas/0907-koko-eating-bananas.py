class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while l<r:
            m=(l+r)//2
            th=sum(math.ceil(i/m)for i in piles)
            if th>h:
                l=m+1
            else:
                r=m
        return l
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        else:
            b=prices[0]
            d=0
            for i in range(1,len(prices)):
                d=max(d,prices[i]-b)
                b=min(b,prices[i])
            return d


        
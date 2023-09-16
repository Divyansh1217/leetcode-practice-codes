class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        if prices[1]+prices[0]<=money:
            return money-(prices[1]+prices[0])
        return money



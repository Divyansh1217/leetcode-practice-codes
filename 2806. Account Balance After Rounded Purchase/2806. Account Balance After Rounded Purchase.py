class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        a=100-purchaseAmount
        b=a%10
        if (b<=5):
            a=a-b
        else:
            a=a+(10-b)
        return a

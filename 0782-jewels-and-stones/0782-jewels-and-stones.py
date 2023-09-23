class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        b=0
        for i in range(len(jewels)):
            a=stones.count(jewels[i])
            b=a+b
        return b

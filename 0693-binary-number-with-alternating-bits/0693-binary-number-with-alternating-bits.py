class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s=str(bin(n))
        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                continue
            else:
                return False
        return True
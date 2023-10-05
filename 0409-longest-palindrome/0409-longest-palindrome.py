class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        count = Counter(s)
        oddFlag = True
        c = 0 
        for v in count.values():
            if v % 2 ==  0:
                c += v
            
            elif v % 2 != 0 and oddFlag:
                c += v
                oddFlag = False
            
            elif v % 2 != 0 and not oddFlag:
                c += (v - 1)
        return c
class Solution:
    def titleToNumber(self,s : str) -> int:
        re=0
        for i in range(len(s)):
            re*=26
            re=re+ ord(s[i]) - ord('A')+1
        return re

class Solution:
    def finalString(self, s: str) -> str:
        a=""
        for k in range(len(s)):
            if s[k]=="i":
                a=a[::-1]
            else:
                a=a+s[k]
        return a
        
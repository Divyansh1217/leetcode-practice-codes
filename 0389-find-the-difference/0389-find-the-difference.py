class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=''.join(sorted(s))
        t=''.join(sorted(t))

        for i in range(len(t)):
            if i >= len(s) and t[i] or i<len(s) and t[i] != s[i]:
                return t[i]
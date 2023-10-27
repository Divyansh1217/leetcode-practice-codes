class Solution:
    def reverse(self, x: int) -> int:
        s='-' if str(x).startswith('-') else ''
        d=int(s+str(abs(x))[::-1])
        if -2**31<=d<=(2**31)-1:
            return d
        return 0


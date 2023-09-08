class Solution:
    def canConstruct(self, a: str,b: str) -> bool:
        a=list(a)
        b=list(b)
        for i in range(len(a)):

            if a[i] not in b:
                return False
            else:
                b.remove(a[i])
        return True
class Solution:
    def canJump(self, n: List[int]) -> bool:
        count=0
        for i in range(len(n)):
            if i > count:
                return False
            count=max(count,i+n[i])
        return True
    
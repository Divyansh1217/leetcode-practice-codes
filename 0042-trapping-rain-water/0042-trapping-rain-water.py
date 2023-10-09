class Solution:
    def trap(self, height: List[int]) -> int:
        s=len(height)
        a=[0]*s
        b=[0]*s
        res=0
        l=0
        r=0
        for i in range(s):
            a[i]=l
            if l<height[i]:
                l=height[i]
        for i in range(s-1,-1,-1):
            b[i]=r
            if r<height[i]:
                r=height[i]
        for i in range(s):
            z=min(a[i],b[i]) - height[i]
            if z>0:
                res=res+z
        return res
     

        
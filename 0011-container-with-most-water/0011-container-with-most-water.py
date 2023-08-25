class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        maxar=0
        right=len(height)-1
        while(left<right):
            cuar=min(height[left],height[right])*(right-left)
            maxar=max(maxar,cuar)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxar
        
        


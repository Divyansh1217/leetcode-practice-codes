class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a=list(sorted((nums))) 
        c=[]
        for i in range(len(nums)):
            b=a.index(nums[i])
            c.append(b)
        return c


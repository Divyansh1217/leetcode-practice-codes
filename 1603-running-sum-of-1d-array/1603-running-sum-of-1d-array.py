class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a=[]
        b=0
        for i in range(len(nums)):
            b=nums[i]+b
            a.append(b)
        return a
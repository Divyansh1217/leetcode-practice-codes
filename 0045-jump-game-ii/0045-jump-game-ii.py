class Solution:
    def jump(self, nums: List[int]) -> int:
        x=[nums[i]+i for i in range(len(nums))]
        i,k,j=0,0,0
        while k<len(nums)-1:
            j=j+1
            i,k=k+1,max(x[i:k+1])
        return j



        
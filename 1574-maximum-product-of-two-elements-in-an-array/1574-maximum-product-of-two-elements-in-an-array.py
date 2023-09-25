class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a=0
        b=[]
        for i in range (len(nums)):
            for j in range(i,len(nums)):
                if i!=j:
                    a=(nums[i]-1) * (nums[j]-1)
                    b.append(a)
        return max(b)


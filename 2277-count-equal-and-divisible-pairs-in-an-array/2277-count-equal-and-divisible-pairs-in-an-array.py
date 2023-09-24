class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        a=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]==nums[j] and i<j and i*j%k==0:
                    a=a+1
        return a
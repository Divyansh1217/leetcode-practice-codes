class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            if nums[i] > i and nums[i-1]<i:
                res += 1
        if 0 not in nums:
            res += 1
        if len(nums) > nums[-1]:
            res += 1
        
        return res

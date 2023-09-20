class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a=0
        for i in range(len(nums)):
            a=a+nums[:i].count(nums[i])
        return a
        
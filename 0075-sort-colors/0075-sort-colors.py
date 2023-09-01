class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        for i in range(n):
            mind=i
            for j in range(i+1,n):
                if (nums[j]<nums[mind]):
                    mind=j
            (nums[i],nums[mind])=(nums[mind],nums[i])

        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=[1]*len(nums)
        pr=1
        po=1
        for i in range(len(nums)):
            a[i]=a[i]*pr
            pr=pr*nums[i]
            a[len(nums)-i-1] *=po
            po=po*nums[len(nums)-i-1]
        return a
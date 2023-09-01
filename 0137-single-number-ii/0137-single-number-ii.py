class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=list(set(nums))
        for i in range (len(a)):
            if nums.count(a[i])==1:
                return a[i]
            else:
                continue
            
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a=sorted(set(nums))
        if len(a)<3:
            return max(nums)
        else:
            b=a.index(max(a))
            return (a[b-2])


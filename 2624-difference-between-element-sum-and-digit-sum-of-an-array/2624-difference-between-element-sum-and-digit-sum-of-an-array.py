class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        res = list(sum(int(i) for i in str(j)) for j in nums)
        a=sum(res)
        b=sum(nums)
        return abs(b-a)
        
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        a=len(nums)
        return sum(
            nums[i] + nums[j] < target
            for i in range(a)
            for j in range(i+1,a)
        )

        
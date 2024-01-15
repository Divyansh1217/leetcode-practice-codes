class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        z, i = set(), len(nums) - 1
        while len(z) < k:
            if nums[i] <= k:
                z.add(nums[i])
            i -= 1
        return len(nums) - i - 1

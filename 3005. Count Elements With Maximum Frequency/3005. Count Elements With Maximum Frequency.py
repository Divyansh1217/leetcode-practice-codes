class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        return sum(v for k,v in Counter(nums).items() if v == Counter(nums).most_common()[0][1])

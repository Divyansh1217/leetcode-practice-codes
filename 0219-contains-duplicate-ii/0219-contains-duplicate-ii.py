class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
      d={}
      a=len(nums)
      for i in range(a):
        if nums[i] in d:
          if abs(d[nums[i]]-i)<=k:
            return True
        d[nums[i]]=i
      return False
        
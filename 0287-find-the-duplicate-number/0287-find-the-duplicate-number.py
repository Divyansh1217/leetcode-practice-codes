class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a={}
        for i ,v in enumerate(nums):
            if v not in a:
                a[v]=1
            else:
                a[v]+=1
        for b,c in a.items():
            if c>1:
                return b
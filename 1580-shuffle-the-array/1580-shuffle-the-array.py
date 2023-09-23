class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a=[]
        j=n
        i=0
        while i<n and j<len(nums):
            a.append(nums[i])
            i=i+1
            a.append(nums[j])
            j=j+1
        return a

        
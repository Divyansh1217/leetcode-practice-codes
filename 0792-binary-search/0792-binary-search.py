class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bina(nums,l,h,target):
            if h>=l:
                m=(l+h)//2
                if nums[m]==target:
                    return m
                elif(nums[m]>target):
                    return bina(nums,l,m-1,target)
                else:
                    return bina(nums,m+1,h,target)
            else:
                return -1
        l=0
        h=len(nums)-1
        ans=bina(nums,l,h,target)
        return ans
        
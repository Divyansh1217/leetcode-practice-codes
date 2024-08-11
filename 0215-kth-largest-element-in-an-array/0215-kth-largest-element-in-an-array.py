class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        x=[]
        
        nums=[-i for i in nums]
        heapq.heapify(nums)
        for i in range(k):
            a=-(heapq.heappop(nums))
            x.append(a)
        return x[-1]

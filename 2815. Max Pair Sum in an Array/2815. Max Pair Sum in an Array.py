class Solution:
    def maxSum(self, nums: List[int]) -> int:
        
        d, ans = defaultdict(list), -1
        
        for num in nums: d[max(str(num))].append(num)  
            
        for ch in d:
            if len(d[ch]) < 2: continue

            ans = max(ans, sum(sorted(d[ch])[-2:]))    

        return  ans     

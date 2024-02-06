class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        beautiful_counter = 0
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return abs(a)
        for i in range(len(nums)-1):
            for j in nums[i+1:]:
                gcd_result = gcd(int(str(nums[i])[0]), j%10)
                if gcd_result == 1:
                    beautiful_counter += 1
        return beautiful_counter

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=i+1
        while j<len(numbers):
            if numbers[i]+numbers[j]==target:
                return [i,j]
            elif j+1==len(numbers):
                i=i+1
                j=i+1
            else:
                j=j+1

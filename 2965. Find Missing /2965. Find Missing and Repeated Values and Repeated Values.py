class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]],b=[0,0]) -> List[int]:
        n=len(a:=Counter(chain(*grid)))+1
        for i in range(1,n+1):
            if a[i] == 1:
                continue
            b[1-a[i]//2]= i
        return b

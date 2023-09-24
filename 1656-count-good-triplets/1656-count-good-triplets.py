class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        d=0
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                for k in range(j,len(arr)):
                    if i<j<k and abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        d=d+1
        return d

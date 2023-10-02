from sortedcontainers import SortedList
class Solution:
    def countRangeSum(self, num: List[int], l: int, u: int) -> int:
        s=SortedList()
        s.add(0)
        z=0
        r=0
        for i in num:
            z=z+i
            lob=z-u
            uop=z-l
            loc=s.bisect_left(lob)
            rof=s.bisect_right(uop)
            r=r+rof-loc
            s.add(z)
        return r
            

        


        
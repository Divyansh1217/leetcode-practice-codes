class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        insort(intervals,newInterval)
        s=[intervals[0]]
        for a,b in intervals[1:]:
            if s [-1][-1] >=a:
                s[-1][-1] = max(s[-1][-1],b)
            else:
                s.append([a,b])
        return s
        
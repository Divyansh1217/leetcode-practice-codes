class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        a=[]
        for i in range(len(grid)):
            x=grid[i].count(1)
            a.append(x)
        return a.index(max(a))

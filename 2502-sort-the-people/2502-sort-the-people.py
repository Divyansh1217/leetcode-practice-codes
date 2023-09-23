class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a=list(set(heights))
        a.sort(reverse=True)
        b=[]
        for i in a:
            for j in range(len(heights)):
                if (heights[j]==i):
                    b.append(names[j])
        return b
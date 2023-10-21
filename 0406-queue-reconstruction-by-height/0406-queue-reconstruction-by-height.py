class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        s=[]
        people.sort(key=lambda x:(-x[0],x[1]))
        for i in people:
            s.insert(i[1],i)
        return s
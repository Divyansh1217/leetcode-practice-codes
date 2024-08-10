class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        a=[]
        n=len(temp)
        res=[0]*len(temp)
        for i in range(n):
            while a and temp[i]>temp[a[-1]]:
                b=a.pop()
                res[b]=i-b
            a.append(i)
        return res
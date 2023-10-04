class Solution:
    def combinationSum(self, s: List[int], key: int) -> List[List[int]]:
        re=[]
        self.dfs(s,key,[],re)
        return re
    def dfs(self,n,key,pa,res):
        if key<0:
            return
        if key==0:
            res.append(pa)
            return
        for i in range(len(n)):
            self.dfs(n[i:],key-n[i],pa+[n[i]],res)
    

        



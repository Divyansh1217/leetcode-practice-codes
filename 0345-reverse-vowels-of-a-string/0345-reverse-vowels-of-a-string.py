class Solution:
    def reverseVowels(self, s: str) -> str:
        q=[]
        n=['a','i','e','o','u','A','E','I','O','U']
        for i in s:
            if i in n:
                q.append(i)
                s=s.replace(i,'*',1)
        q.reverse()
        k=0
        for i in s:
            if i=="*":
                s=s.replace("*",q[k],1)
                k=k+1
        return s
            
    


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=[]
        b=[]
        if len(s)==0:
            return 0
        else:
            for j in range(len(s)):
                c=0
                b.clear()
            
                for i in range(j,len(s)):
                    if s[i] not in b:
                        b.append(s[i])
                        c=c+1
                        a.append(c)
                    else:
                        break
        return max(a)
                     
        

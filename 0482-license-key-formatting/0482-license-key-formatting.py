class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.replace("-","").upper()
        a=len(s) %  k
        re=s[:a]
        for i in range(a,len(s),k):
            if re:
                re=re+"-"
            re=re+s[i:i+k]
        return re

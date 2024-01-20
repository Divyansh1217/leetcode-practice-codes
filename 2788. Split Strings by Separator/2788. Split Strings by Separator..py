class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        b=[]
        for i in words:
            a=i.split(separator)
            for j in a:
                if j:
                    b.append(j) 
        return b

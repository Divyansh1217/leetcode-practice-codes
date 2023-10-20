class Solution:
    def convert(self, s: str, n: int) -> str:
        if n==1 or n>=len(s):
            return s
        rows = [[] for row in range(n)]
        index = 0
        step = -1
        for char in s:
            rows[index].append(char)
            if index == 0:
                step = 1
            elif index == n - 1:
                step = -1
            index += step

        for i in range(n):
            rows[i] = ''.join(rows[i])
        return ''.join(rows)    
        
        
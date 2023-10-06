class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1="qwertyuiop"
        row2="asdfghjkl"
        row3="zxcvbnm"
        ans = []

        for word in words:
            flag = 0
            temp = word
            word = word.lower()
            if word[0] in row1:
                res_row = row1
            elif word[0] in row2:
                res_row = row2
            else:
                res_row = row3
            for i in range(0, len(word)):
                if word[i] not in res_row:
                    flag = 1
                    break
            if flag == 0:
                ans.append(temp)
        return ans

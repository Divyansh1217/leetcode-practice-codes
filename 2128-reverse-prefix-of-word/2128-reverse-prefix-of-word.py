class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        a=''
        b=0
        for i in range(len(word)):
            b=b+1
            a=a+word[i]
            if word[i]==ch:
                a=a[::-1]
                break
        for i in range(b,len(word)):
            a=a+word[i]
        return a

        


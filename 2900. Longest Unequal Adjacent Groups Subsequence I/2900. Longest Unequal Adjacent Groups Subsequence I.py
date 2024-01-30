class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        a=[words[0]]
        b=groups[0]
        for i in range(1,n):
           if groups[i] != b:
               a.append(words[i])
               b=groups[i]
        return a

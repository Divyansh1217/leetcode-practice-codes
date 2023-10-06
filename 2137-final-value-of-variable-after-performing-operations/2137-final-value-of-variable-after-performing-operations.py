class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        a={"--X":-1,"X--":-1,"X++":1,"++X":1}
        s=0
        for i in range(len(operations)):
            s=s+a.get(operations[i])
        return s
        
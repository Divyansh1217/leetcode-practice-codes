class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        a=len(matrix)
        b=len(matrix[0])
        arr=[]
        for i in range(a):
            for j in range(b):
                if matrix[i][j]==0:
                    arr.append([i,j])
        for k,l in arr:
            for row in range(b):
                matrix[k][row]=0
            for col in range(a):
                matrix[col][l]=0

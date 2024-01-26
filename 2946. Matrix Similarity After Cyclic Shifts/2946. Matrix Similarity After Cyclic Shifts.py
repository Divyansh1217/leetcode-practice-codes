class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        mat1=[i[:] for i in mat]
        for i in range(k):
            for j in range(len(mat)):
                temp=mat[j][0]
                for k in range(len(mat[0])-1): 
                    mat[j][k]=mat[j][k+1]
                mat[j][-1]=temp 

        if  mat==mat1:
            return (True)
        else:
            return (False)

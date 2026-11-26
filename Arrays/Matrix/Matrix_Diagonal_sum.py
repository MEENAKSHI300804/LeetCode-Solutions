class Solution(object):
    def diagonalSum(self, mat):
        r1=len(mat)
        total=0
        for i in range(r1):
            total+=mat[i][i]
            if i!=r1-1-i:
                total+=mat[i][r1-1-i]
        return total
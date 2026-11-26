class Solution(object):
    def transpose(self, matrix):
        r1=len(matrix)
        c1=len(matrix[0])
        result=[]
        for i in range(c1):
            row=[]
            for j in range(r1):
                e=matrix[j][i]
                row.append(e)
            result.append(row)
        return result
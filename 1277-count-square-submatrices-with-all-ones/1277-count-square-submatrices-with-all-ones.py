class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]==0:
                    continue
                val=min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])
                matrix[i][j]+=val
        s=0
        print(matrix)
        for i in matrix:
            s=s+sum(i)
        return s
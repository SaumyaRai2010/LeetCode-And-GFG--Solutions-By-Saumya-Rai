class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        mat=[[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j+k<len(grid[0]):
                    mat[i][j+k]=grid[i][j]
                elif j+k >= len(grid[0]):
                    right_shift=(j+k)%len(grid[0])
                    down_shift=(i+((j+k)//len(grid[0])))%len(grid)
                    mat[down_shift][right_shift]=grid[i][j]
        return mat
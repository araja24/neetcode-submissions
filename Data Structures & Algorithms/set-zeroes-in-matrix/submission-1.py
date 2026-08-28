class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        m = len(matrix) # rows
        n = len(matrix[0]) # cols

        rows0 = []
        cols0 = []


        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows0.append(i)
                    cols0.append(j)
        
        for row in rows0:
            for col in range(n):
                matrix[row][col] = 0
        


        for col in cols0:
            for row in range(m):
                matrix[row][col] = 0

        



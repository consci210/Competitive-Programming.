class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.arr = matrix
        self.rows , self.cols = len(matrix) , len(matrix[0])
        self.prefixSum = [[0 for _ in range(self.cols + 1)] for _ in range(self.rows + 1)]
        for row in range(1,self.rows+1):
            for col in range(1,self.cols+1):
                self.prefixSum[row][col] = self.prefixSum[row-1][col] + self.prefixSum[row][col-1] - self.prefixSum[row-1][col-1] + self.arr[row-1][col-1]
         
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        answer = self.prefixSum[row2+1][col2+1] - self.prefixSum[row2+1][col1] - self.prefixSum[row1][col2+1] + self.prefixSum[row1][col1]
        return answer
         
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
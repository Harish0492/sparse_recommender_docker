# sparse_recommender.py

class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = {}  

    def set(self, row, col, value):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError("Invalid matrix ")
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]

    def get(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError("Invalid matrix ")
        return self.data.get((row, col), 0)

    def recommend(self, vector):
        if len(vector) != self.cols:raise ValueError("User vector do not match matrix dimensions for multiplication")

        recommendations = [0] * self.rows
        for row in range(self.rows):
            for col in range(self.cols):
                recommendations[row] += self.get(row, col) * vector[row]  
                return recommendations


    def add_movie(self, matrix):
        if self.rows != matrix.rows or self.cols != matrix.cols:
            raise ValueError("Matrix dimensions do not match for addition")

        resultMovie = SparseMatrix(self.rows, self.cols)

        for (row, col), value in self.data.items():
            resultMovie.set(row, col, value)

        for (row, col), value in matrix.data.items():
            resultMovie.set(row, col, resultMovie.get(row, col) + value)

        return resultMovie

    def to_dense(self):
        denseMatrix = [[0] * self.cols for _ in range(self.rows)]
        for (row, col), value in self.data.items():
            denseMatrix[row][col] = value
        return denseMatrix

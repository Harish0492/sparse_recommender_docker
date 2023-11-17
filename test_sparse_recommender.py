# test_sparse_recommender.py

import pytest
from sparse_recommender import SparseMatrix

def test_set_and_get_value():
    matrix = SparseMatrix(2, 2)
    matrix.set(0, 0, 5)
    assert matrix.get(0, 0) == 5

def test_get():
    matrix = SparseMatrix(2, 2)
    assert matrix.get(1, 1) == 0

def test_recommend():
    matrix = SparseMatrix(3, 3)
    matrix.set(0, 0, 1)
    matrix.set(1, 1, 2)
    matrix.set(1, 1, 3)
    user_vector = [0.5, 1.0, 0.2]
    recommendations = matrix.recommend(user_vector)
    assert recommendations == [0.5, 0, 0]

def test_recommend1():
    matrix = SparseMatrix(2, 2)
    matrix.set(0, 0, 1)
    matrix.set(1, 1, 2)
    
    user_vector = [0.5, 1.0]
    recommendations = matrix.recommend(user_vector)
    assert recommendations == [0.5, 0] 

def test_recommend2():
    matrix = SparseMatrix(4, 4)
    matrix.set(1,0 , 1)
    matrix.set(1, 0, 2)
    
    user_vector = [0.5, 0.0,1.0,0]
    recommendations = matrix.recommend(user_vector)
    assert recommendations == [0.0, 0,0,0]           

def test_add_movie():
    matrix1 = SparseMatrix(2, 2)
    matrix1.set(0, 0, 1)
    matrix1.set(1, 1, 1)
    matrix1.set(1, 0, 5) 
    matrix1.set(0, 1, 5) 

    matrix2 = SparseMatrix(2, 2)
    matrix2.set(0, 0, 3)
    matrix2.set(1, 0, 1)
    matrix2.set(1, 1, 5) 
    matrix2.set(0, 1, 3) 

    updatedMatrix = matrix1.add_movie(matrix2)
    assert updatedMatrix.get(0, 0) == 4
    assert updatedMatrix.get(0, 1) == 8
    assert updatedMatrix.get(1, 0) == 6
    assert updatedMatrix.get(1, 1) == 6

def test_add_movie1():
    matrix1 = SparseMatrix(2, 2)
    matrix1.set(0, 0, 3)
    matrix1.set(1, 1, 5) 
    matrix1.set(0, 1, 4) 
    matrix1.set(1, 0, 5) 


    matrix2 = SparseMatrix(2, 2)
    matrix2.set(0, 0, 6)
    matrix2.set(1, 0, 3)
    matrix2.set(1, 1, 3)
    
    updatedMatrix = matrix1.add_movie(matrix2)
    assert updatedMatrix.get(0, 0) == 9
    assert updatedMatrix.get(0, 1) == 4
    assert updatedMatrix.get(1, 0) == 8
    assert updatedMatrix.get(1, 1) == 8

def test_to_dense():
    matrix = SparseMatrix(2, 3)
    matrix.set(0, 0, 1)
    matrix.set(1, 2, 2)
    matrix.set(0, 2, 2)
    matrix.set(1, 1, 3)
    denseMatrix = matrix.to_dense()
    assert denseMatrix == [[1, 0, 2], [0, 3, 2]]





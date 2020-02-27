import numpy as np

A = np.array([ [1,1,2,11],
               [3,5,8,11],
               [1,2,3,11],
               [2,2,2,11]])

B = np.array([ [2,3,5,12],
               [7,11,13,12],
               [4,5,6,12],
               [3,3,3,12]
               ])

C = np.array([
             [3,1,4],
             [1,5,9],
             [2,6,5],
             [3,5,6]
    ])
print ("Addition :")
print (A + B)
print ("Subtraction :")
print (A - B)

print ("Scalar Multiplication ")
print (C * 100)

print("Multiplication using *")
print(A * B)

print("Multiplication using Dot")
print(A.dot(B))

print ("Transpose of Matrix")
print (np.transpose(C))

print("First Row Of Matrix C")
row_1_C = C[0]
print (row_1_C)

print("Matrix C : [32] element")
threeTwoIndex = C[3,2]
print (threeTwoIndex)

print("Concatinate A and B vertically")
combineMatrixRow = np.concatenate((A,B), axis=0)
print (combineMatrixRow)

print("Concatinate A and B Horizontally")
combineMatrixColumn = np.concatenate((A,B), axis=1)
print (combineMatrixColumn)


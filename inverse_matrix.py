from colors import bcolors
from matrix_utility import row_addition_elementary_matrix, scalar_multiplication_elementary_matrix
import numpy as np

"""
Function that find the inverse of non-singular matrix
The function performs elementary row operations to transform it into the identity matrix. 
The resulting identity matrix will be the inverse of the input matrix if it is non-singular.
 If the input matrix is singular (i.e., its diagonal elements become zero during row operations), it raises an error.
"""


def inverse(matrix):
    print(bcolors.OKBLUE, f"=================== Finding the inverse of a non-singular matrix using elementary row operations ===================\n {matrix}\n", bcolors.ENDC)
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix must be square.")

    n = matrix.shape[0]
    identity = np.identity(n)
    counter = 0

    # Perform row operations to transform the input matrix into the identity matrix
    for i in range(n):
        if matrix[i, i] == 0 :
            raise ValueError("Matrix is singular, cannot find its inverse.")

        if matrix[i, i] != 1:
            # Scale the current row to make the diagonal element 1
            scalar = 1.0 / matrix[i, i]
            elementary_matrix = scalar_multiplication_elementary_matrix(n, i, scalar)
            if counter >7:
                print(f"elementary matrix to make the diagonal element 1 :\n {elementary_matrix} \n")
                matrix = np.dot(elementary_matrix, matrix)
            counter+=1

                #print(f"The matrix after elementary operation :\n {matrix}")
                #print(bcolors.OKGREEN, "------------------------------------------------------------------------------------------------------------------",  bcolors.ENDC)
                #identity = np.dot(elementary_matrix, identity)



        # Zero out the elements above and below the diagonal
        for j in range(n):
            if i != j:
                scalar = -matrix[j, i]
                elementary_matrix = row_addition_elementary_matrix(n, j, i, scalar)
                if counter >7:
                    print(f"elementary matrix for R{j+1} = R{j+1} + ({scalar}R{i+1}):\n {elementary_matrix} \n")
            counter += 1
                    #matrix = np.dot(elementary_matrix, matrix)
                    #print(f"The matrix after elementary operation :\n {matrix}")
                    #print(bcolors.OKGREEN, "------------------------------------------------------------------------------------------------------------------",bcolors.ENDC)
                    #identity = np.dot(elementary_matrix, identity)


    return identity


if __name__ == '__main__':
    """"
    Date: 19/2/24
    Group: Avishag Tamssut id-326275609
            Merav Hashta id-214718405
            Sahar Emmuna id-213431133
    Git: https://github.com/Avishagtams/test1.py.git
    Name: Merav Hashta id-214718405
    input:

    """

    A = np.array([[1, 10, -10],
                  [0, 4, 6],
                  [0, 1, 9]])
    """
    A = np.array([[2, 1, 0, 0],
                  [3, 2, 0, 0],
                  [1, 1, 3, 4],
                  [2, -1, 2, 3]])
    """

    try:
        A_inverse = inverse(A)
        print(bcolors.OKBLUE, "\nInverse of matrix A: \n", A_inverse)
        print("=====================================================================================================================", bcolors.ENDC)

    except ValueError as e:
        print(str(e))



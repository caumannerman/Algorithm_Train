
def rotate_Matrix_90clockwise(matrix):
    # nxm size matrix
    n = len(matrix)
    m = len(matrix[0])
    result = [[0]*n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-1-i] = matrix[i][j]
    return result



def rotate_Matrix_90CounterClockwise(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = [[0]*n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[m-1-j][i] = matrix[i][j]

    return result


def show_matrix(mat):
    for i in mat:
        print(i)

a = [[1,2,3,4,5],[2,5,2,6,7],[11,5,9,0,2]]



print(show_matrix(a))
print(show_matrix(rotate_Matrix_90clockwise(a)))
print("=======================")
print(show_matrix(rotate_Matrix_90CounterClockwise(a)))
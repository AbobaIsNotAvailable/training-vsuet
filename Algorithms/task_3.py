def matrix_is_magic(matrix):
    n = sum(matrix[0])
 
    for i in range(len(matrix)):
        num = 0
        for j in range(len(matrix)):
            num += matrix[j][i]
        if num != n or sum(matrix[i]) != n:
            return False
    return True
 
 
mat = [[4, 3, 3],
        [3, 4, 3],
        [3, 3, 4]]
        
print(matrix_is_magic(mat))




def per_matix(mat):
    mat_first = mat[0]
    mat_last = mat[::-1][0]

    mat.pop(0)
    mat.pop(len(mat) - 1)

    mat.insert(0, mat_last)
    mat.append(mat_first)

    print(mat)
    

matrix = [[1, 2, 3, 4],
[5, 6, 7, 8],
[9,10,11,12],
[5, 6, 7, 8]]

per_matix(matrix)
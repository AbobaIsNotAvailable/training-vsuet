import json


def read_from_file():

    with open("GrebenshikovPavel_ZIT-2022_vivod.json", encoding="utf-8", mode="r+") as rf:
        data = json.load(rf)
        return data

def matrix_is_magic(matrix):

    if matrix is None:
        return

    print(type(matrix))

    n = sum(matrix[0])
 
    for i in range(len(matrix)):
        num = 0
        for j in range(len(matrix)):
            num += matrix[j][i]
        if num != n or sum(matrix[i]) != n:
            return False
    return True
 
matrix_is_magic(read_from_file())


def per_matix(mat):

    # print(mat)

    mat_first = mat[0]
    mat_last = mat[::-1][0]

    mat.pop(0)
    mat.pop(len(mat) - 1)

    mat.insert(0, mat_last)
    mat.append(mat_first)

    with open("GrebenshikovPavel_ZIT-2022_vvod.json", encoding="utf-8", mode="w+") as fw:
        json.dump(mat, fw)

per_matix(read_from_file())

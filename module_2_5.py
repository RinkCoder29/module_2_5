def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        list_ = []
        for j in range(m):
            list_.append(value)
        matrix.append(list_)
    return matrix

mat = get_matrix(5,3,29)
print(mat)



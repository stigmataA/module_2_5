def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix.append(value)
    print(matrix)
get_matrix(3,5, 42)
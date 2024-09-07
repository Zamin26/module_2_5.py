def get_matrix (n,m,value):
    matrix = []
    for i in range(n):
        line = []
        matrix.append(line)
        for k in range(m):
            line.append(value)
    return matrix
result1 = get_matrix(2, 3, 9)
result2 = get_matrix(3, 4, 10)
result3 = get_matrix(4, 5, 11)
print(result1)
print(result2)
print(result3)

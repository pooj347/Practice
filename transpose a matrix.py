matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rows = len(matrix)
cols = len(matrix[0])

transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

for i in range(rows):
    for j in range(cols):
        transposed_matrix[j][i] = matrix[i][j]

print(transposed_matrix)

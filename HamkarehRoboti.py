import numpy as np

with open('input.txt', 'r') as f:
    input_str = f.read()

input_list = list(map(int, input_str.split()))

num_matrices = input_list[0]
matrix_size = input_list[1]

matrices = []

for i in range(num_matrices):
    matrix = []
    for j in range(matrix_size):
        row = list(map(int, input().split()))
        matrix.append(row)
    matrices.append(matrix)


def sort_matrices_by_determinant(matrices):
    return sorted(matrices, key=lambda x: np.linalg.det(x))

sorted_matrices = sort_matrices_by_determinant(matrices)

if  np.linalg.det(sorted_matrices[1])* np.linalg.det(sorted_matrices[0])> np.linalg.det(sorted_matrices[-1])*np.linalg.det(sorted_matrices[-2]):
    biggest_multiplication=np.dot(sorted_matrices[1], sorted_matrices[0])
else:
     biggest_multiplication=np.dot(sorted_matrices[-1], sorted_matrices[-2])

inverse = np.linalg.inv(biggest_multiplication)
print(inverse)

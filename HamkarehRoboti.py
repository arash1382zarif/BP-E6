#!/usr/bin/env python3
# Author: Arash Zarif

import numpy as np


def read_matrices(file_path):
    with open(file_path, 'r') as f:
        input_str = f.read()

    input_list = list(map(int, input_str.split()))

    num_matrices = input_list[0]
    matrix_size = input_list[1]

    matrices = []

    for _ in range(num_matrices):
        matrix = []
        for _ in range(matrix_size):
            row = list(map(int, input().split()))
            matrix.append(row)
        matrices.append(matrix)

    return matrices


def sort_matrices_by_determinant(matrices):
    return sorted(matrices, key=lambda x: np.linalg.det(x))


def main():
    file_path = 'input.txt'
    matrices = read_matrices(file_path)

    sorted_matrices = sort_matrices_by_determinant(matrices)

    det_first_two = np.linalg.det(sorted_matrices[1]) * np.linalg.det(sorted_matrices[0])
    det_last_two = np.linalg.det(sorted_matrices[-1]) * np.linalg.det(sorted_matrices[-2])

    biggest_multiplication = np.dot(sorted_matrices[1], sorted_matrices[0]) if det_first_two > det_last_two else np.dot(
        sorted_matrices[-1], sorted_matrices[-2])

    inverse = np.linalg.inv(biggest_multiplication)
    print(inverse)


if __name__ == "__main__":
    main()

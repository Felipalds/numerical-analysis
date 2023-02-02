import sys

def pivoting(matrix, l):
    for i in range(len(matrix) - 1):
        for j in range(len(matrix) - 1):
            if matrix[l][l] < matrix[i][i] and i > l:
                aux = matrix[l]
                matrix[l] = matrix[i]
                matrix[i] = aux

print("Gauss elimination method!")

matrix_coefficients = int(input("Enter number of coeficients: "))
matrix = []
answers = []

for i in range(matrix_coefficients):
    answers.append(0)

for i in range(matrix_coefficients):
    matrix_line = []
    for j in range(matrix_coefficients + 1):
        matrix_line.append(int(input((f"[{i + 1},{j + 1}]: "))))
    matrix.append(matrix_line)
print(matrix)

# Applying Gauus Elimination:
for i in range(matrix_coefficients):
    pivoting(matrix, i)
    if matrix[i][i] == 0:
        sys.exit("Division by zero detected")

    for j in range(i + 1, matrix_coefficients):
        ratio = matrix[j][i] / matrix[i][i]
        print(matrix[j][i], "/", matrix[i][i], " == ", ratio)

        for k in range(matrix_coefficients+1):
            matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

print(matrix)
answers[matrix_coefficients - 1] = matrix[matrix_coefficients - 1][matrix_coefficients] / matrix[matrix_coefficients - 1][matrix_coefficients - 1]

for i in range (matrix_coefficients -2, -1, -1):
    answers[i] = matrix[i][matrix_coefficients]

    for j in range(i + 1, matrix_coefficients):
        answers[i] = answers[i] - matrix[i][j] * answers[j]

    answers[i] = answers[i]/matrix[i][i]

for i in range(matrix_coefficients):
    print(answers[i])



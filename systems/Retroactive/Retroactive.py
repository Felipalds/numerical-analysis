

A = [[2, 3, -1, 5], [0, -2, -1, -7], [0, 0, 5, 15]]
x = [0, 0, 0]
m = len(A) - 1
n = len(A[0]) - 1
s = 0

x[m] = A[m][n] / A[m][m]

for k in range(m, 1, -1):
    s = 0
    print(k)

    for j in range(k, m+1):
        print(j)
        s = s + A[k][j] * x[j]
    x[k] = (A[k][n] - s) / A[k][k]
    
print(x)



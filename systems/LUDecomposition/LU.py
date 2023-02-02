n = int(input("Insira o número de índices de sua matriz: "))
matrix = []
identity = []

for i in range(n):
    row = []
    identity_row = []
    for j in range(n):
        row.append(int(input(f"{i}, {j}: ")))
        if(i == j):
            identity_row.append(1)
        else:
            identity_row.append(0)

    identity.append(identity_row)
    matrix.append(row)
print(identity)




clear
clc

A = [2 3 -1 5; 4 4 -3 3; 2 -3 1 -1];

[m, n] = size(A)
B = A

for k = 1 : (m - 1)
    for i = (k + 1):m
        mult = A(i,k)/A(k,k)
        A(i, k) = 0

        for j = (k + 1):n
            A(i, j) = A(i, j) - mult * A(k, j)
        end
    end
end

disp(A, 'matriz triangular superior')
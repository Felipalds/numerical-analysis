def newton(x, y, xi):
   n = len(x)
   tabela = [[None for x in range(n)] for x in range(n)]
   
   for i in range(n):
       tabela[i][0] = y[i]
       
   for j in range(1, n):
       for i in range(n - j):
           tabela[i][j] = (tabela[i+1][j-1] - tabela[i][j-1])/(x[i+j] - x[i])
   somax = 1
   p = tabela[0][0]
   
   for order in range(1, n):
       somax = somax*(xi - x[order - 1])
       p = p + tabela[0][order]*somax
   
   
   return p
valorX = [1, 2, 3, 5]
fdex = [-2, 4 , 28, 46]
xp = 0.50000
print(newton(valorX, fdex, xp))
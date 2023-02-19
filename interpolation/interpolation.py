listaX = []
listaY = []
 
def lagrange(x, y):
       coeficientes = []
       for i in range(0,3):
           produto = 1
           for j in range(0,3):
               if i != j:
                   produto *= (x[i] - x[j])
           coef = y[i]/ produto
           coeficientes.append(coef)
       return coeficientes
 
def polinomiolagrange(x, lista, coeficienteslista) -> float:
   s = 0
   aux = len(coeficienteslista)
   for i in range(aux):
       produto = 1
       for j in range(aux):
           if i != j:
               produto *= (x - lista[j])
       produto *= coeficienteslista[i]
       s += produto
   return s
   
print("Digite o valores do 1º ponto:")
for i in range(0, 2):
   counter = i + 1
   if(counter == 1):
       print("Digite o valor de X:")
       x = float(input())
       listaX.append(x)
   else:
       print("Digite o valor de Y:")
       y = float(input())
       listaY.append(y)
 
print("Digite o valores do 2º ponto:")
for i in range(0, 2):
   counter = i + 1
   if(counter == 1):
       print("Digite o valor de X:")
       x = float(input())
       listaX.append(x)
   else:
       print("Digite o valor de Y:")
       y = float(input())
       listaY.append(y)
 
print("Digite o valores do 3º ponto:")
for i in range(0, 2):
   counter = i + 1
   if(counter == 1):
       print("Digite o valor de X:")
       x = float(input())
       listaX.append(x)
   else:
       print("Digite o valor de Y:")
       y = float(input())
       listaY.append(y)
 
c = lagrange(listaX, listaY)
 
segundograu = polinomiolagrange(1, listaX, c) * -1
primeirograu = polinomiolagrange(4, listaX, c) * - 1
grau0 = polinomiolagrange(2, listaX, c) * - 1
print("Polinomio:")
print(segundograu,"x²", primeirograu,"x", grau0)
print("calcular determinante de una matriz 2x2")

print("valor de x y y en la matriz 2x2")
M1 = input("ingresar el de x en la posición 1,1 en la matriz")
M2 = input("ingresar el de x en la posición 1,2 en la matriz")
M3 = input("ingresar el de x en la posición 2,1 en la matriz")
M4 = input("ingresar el de x en la posición 2,2 en la matriz")

M1 = float(M1)
M2 = float(M2)
M3 = float(M3)
M4 = float(M4)

Determinante = ((M1 * M4) - (M2 * M3))

print("La determinante de la matriz es :,"+ Determinante)

 
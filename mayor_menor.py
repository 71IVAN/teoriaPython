n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

calcular = lambda  n1, n2 : n1 if n1 > n2 else n2

if n1 == n2: print("Los numeros son iguales")

else: 
   resultado = calcular(n1, n2)

print(f"El numero mayor es : {resultado}")
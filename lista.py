modulos = ["Logica","Base Datos","HTML5", "Moviles", "HTML5"]
print(modulos)

#print("Elemento final de la lista es ===========> " , modulos[-1])
#print("Nro de elementos que contienen la lista =>" , len(modulos[3]))
#print("ultimo elemento de la lista =============>" , modulos[len(modulos)-1])

#print("Agregar un elemento a lista..Metologicas agiles ")
#modulos.append("Metodologias agiles")
#print(modulos)
#modulos.insert(2, "php")
#print(modulos)
#cantidad de veces que se repite un elemento en la lista
#Cantidad de veces que se repote un elemento en la lista
print("Cantidad de veces que aparece HTML5 ===> " , modulos.count("HTML5"))

print("Lista Ordenada alfabeticamente")
modulos.sort()
print(modulos)

for indice in modulos:
    print(indice)
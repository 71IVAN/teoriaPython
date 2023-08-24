mensaje = "      Bienvenido ... al curso de python"

# metodo len, imprime el tamaño de longitud del string, contando los espacios 
#print("El tamaño del texto es de : ", len(mensaje) , "caracteres") 

# strip, quita espacios al inicio y al final
sinEspacios = mensaje

#print("Texto sin espacios : ", sinEspacios.strip())

#print("Tamaño del texto sin espacio es de : " , len(sinEspacios))

#upper para mayusculuas sostenida
#print(sinEspacios.upper())

#lower para minuscula en todo el texto
#print("", sinEspacios.lower())

#title, primera inicial de cada palabra inprime en Mayuscula 
#print("", sinEspacios.title())

#capitalize, solo imprime la primera inicial en mayuscula de la primera palabra
#print( sinEspacios.capitalize())


parrafo = sinEspacios.split("...")
print(parrafo[0])
print(parrafo[1])


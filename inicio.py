print("---- Calcular nota definitiva-----")
name = input("Nombre del estudiante: ")
nota1 = float(input("Nota uno: "))
nota2 = float(input("Nota dos: "))
nota3 = float(input("Nota tres: "))
definitiva = (nota1 + nota2 + nota3)/3
print("Nombre: ", name , "\n Nota 1 -->", nota1, "Nota 2 -->" , nota2, "Nota 3 -->", nota3, "La definitiva es : " , definitiva)

if definitiva < 0 or  definitiva > 5:
    print("Error nota no valida" )
    
elif definitiva >= 0 or definitiva <3: 
    print ("Tiene opcion de recuperar ")
    
elif definitiva >= 3 or definitiva < 4:
    print ("Ganaste")
    
elif definitiva >=4 or definitiva <= 5:
    print ("Eres la hostia tio")
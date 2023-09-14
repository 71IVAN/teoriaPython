#Funcion sin parametros y no devuelve nada

def Saludar():
    print("Welcome Merry estas en Python ")

def SaludarName(nombre):
     print(f"Hola {nombre}, estas bien ? ")
     
     
def Programa(nombre, nota):
    print(f"Hola {nombre}, tines una nota de {nota}")
    print("Hola ", nombre, " tienes una nota de ", nota)
    
def ProgramaDefault(nombre, nota, progrma="Nevas tecnologias"):
    print(f"Hola {nombre}, tines una nota de {nota} en el modulo de {progrma}")
    
    
def Operaciones(n1, n2):
   return (n1 + n2, n1 * n2) 
   

#llamar las funciones
if __name__ == "__main__":
#    SaludarName("Merry")
#    user = "Derrick Rose"
#    SaludarName(user)
  resultado = Operaciones(5,10)
  n1 = 7
  n2 = 2
  print (resultado)
  print(f"{n1} + {n2} = {resultado[0]}")
  print(f"{n1} + {n2} = {resultado[1]}")
#   ProgramaDefault("Mauricio", 2.9, "PHP")
#   ProgramaDefault("Alvaro", 1.5)
   
   #Saludar() 

def sum(nmr1, nmr2):   return nmr1 + nmr2

sumando = lambda nr1, nr2: nr1 + nr2

def rest():
    pass

if __name__=="__main__":
    print (sum(123, 788))

    nmr1 = int(input("Numero 1: "))
    nmr2 = int(input("Numero 2: "))

    print(sum(nmr1, nmr2))

    print(  sumando(nmr1, nmr2),"Funcion lambda") 
#Para saber si un año es bisiesto este tiene que ser múltiplo de 4 
#Si es múltiplo de 4 y de 100 no es bisiesto
#Pero si es múltiplo de 400 si es Bisiesto

def Bisiesto(year):
    if year % 4 != 0:
        print("No Bisiesto")
    elif year % 4 == 0 & year % 100 !=0:
        print("Bisiesto")
    elif year % 4 == 0 & year % 100 == 0 & year % 400 !=0:
        print("No es Bisiesto")
    elif year % 4 == 0 & year % 100 == 0 & year % 400 ==0:
        print("Bisiesto")
        

Bisiesto(1980)
    
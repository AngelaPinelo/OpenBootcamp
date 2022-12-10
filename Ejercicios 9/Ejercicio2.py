from functools import reduce

def Funcion(numeros): 
    resultado = list(filter((lambda x: x % 2), numeros)) 
    print(resultado)
    resultado = reduce( (lambda x, y: x + y), resultado) 
    print(resultado)

listanum = list(range(100))

Funcion(listanum)
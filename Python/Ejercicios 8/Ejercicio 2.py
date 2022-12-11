from pickle import *

class Vehiculo:

    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas

    def __str__(self):
        return "Carro color " + self.color + " Puertas: " + self.puertas


corsa = Vehiculo("Azul", "4")
Pichi = Vehiculo("Gris","5")
print(corsa)

file = open('Archivo ejercico 82', 'w+b')

dump(Pichi, file)

file.seek(0)
nuevoCarro = load(file)

print(nuevoCarro)
file.close()

class Vehiculo():
    
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    

class Coche(Vehiculo):

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    

coche = Coche("rojo", 4, 4, 200, 700)
print("El coche es color " + coche.color + " tiene "+str(coche.ruedas)+ " ruedas y "+str(coche.puertas)+" puertas, velodidad de "+str(coche.velocidad)+" y cilindrada de "+str(coche.cilindrada))
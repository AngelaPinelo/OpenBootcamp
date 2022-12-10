class Alumno():
    def Iniciar(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        
    def Imprimir(self):
        print("Nombre del alumno: "+ self.nombre)
        print("Nota: "+ str(self.nota))
    
    def Aprobado(self):
        if self.nota >= 61:
            print("Aprobado")
        else:
            print ("No Aprobado")


alumno1 = Alumno()
alumno2 = Alumno()

alumno1.Iniciar("Gabriela", 87)
alumno1.Imprimir()
alumno1.Aprobado()

alumno2.Iniciar("Sergio", 57)
alumno2.Imprimir()
alumno2.Aprobado()
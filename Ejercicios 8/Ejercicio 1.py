file = open('Ejercicio81.txt', 'w')
file.write('Hola!')
file.close()

file = open('Ejercicio81.txt', 'r+')
file.readline()
file.write('Adios!.')

file.seek(0)
print(file.read())
file.close()
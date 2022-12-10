paises = input("Introduce países separados por comas:\n")

almacen=[paises.split(",")]
print(almacen[0])

print(sorted(set(almacen[0])))


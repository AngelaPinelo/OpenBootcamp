import time


#damos formato a la hora
horas = time.strftime('%H') 
minutos = time.strftime('%M') 

#hora de salida 7 pm

if int(horas)>= 19:
    print("Hora de ir a casa")
else:
    print("Son las "+horas+" horas con "+ minutos+" minutos")
    print("Faltan "+str(18-int(horas))+" horas y "+ str(59 -int(minutos))+" minutos para ir a casa")

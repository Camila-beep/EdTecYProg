#esta es la primer etapa, donde cargo todas las variables y me aseguro de que estén bien cargadas
print("Ingresa cuantos partidos ganaron ")
ganados = int(input())
print("Ingresa cuantos partidos perdieron ")
perdidos = int(input())
print ("Ingresa cuantos partidos empataron ")
empatados = int(input())

#en la segunda etapa calculo el puntaje final y lo muestro
puntaje = ganados*3 + perdidos*1 + empatados*0

print("Su resultado final es de: ",puntaje)

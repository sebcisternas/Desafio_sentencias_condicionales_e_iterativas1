import math

weight = int(input("Ingrese Peso en [kg] = "))
height = int(input("Ingrese Altura en [cm] = ")) 

height_m = height/100.0

imc= weight/(height_m**2)

if imc<18.5:
     clasificacion = "Bajo Peso"
     
elif imc>=18.5 and imc<25:
     clasificacion = "Adecuado"
     
elif imc>=25 and imc<30:
     clasificacion = "Sobrepeso"
     
elif imc>=30 and imc<35:
     clasificacion = "Obesidad Grado 1"
     
elif imc>=35 and imc<40:
     clasificacion = "Obesidad Grado 2"
     
else:
     clasificacion = "Obesidad Grado 3"
     
print(f"Su IMC es {imc:.2f}")
print(f"La clasificación OMS es {clasificacion}")

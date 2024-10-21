print("¿Cuál es tu huella de carbono?, ¿Cuántos aárboles necesitarías plantar para cubrirla?, ¡Vamos a descubrirla!")
print("Contesta las siguiente preguntas")

Total=0.0

#LUZ

luzm=float(input("¿Cúantos KwH consumes al mes?\n"))
Total=luzm*0.5

FR=float(input("¿Qué porcentaje de tu electricidad proviene de fuentes renovables? (INDIQUE CON UN PORCENTAJE DE 0% AL 100%) \n")) 
if FR==0 :
    Total=Total*10
elif FR==100:
    Total=0
else:
    FRT=FR/100
    FRT1=Total*FRT
    Total=Total-FRT1

#GAS

TP=input("¿Cúal medio de transporte usas normalmente? (Bicicleta, Caminar, transporte público, Automóvil(Gasolina diesel), Motocicleta, Camioneta \n")
if TP=="bicicleta" or "caminar":
    Total=Total+0
if TP=="transporte público":
    Total=Total+100
if TP=="Motocicleta":
    Total=Total+250
if TP=="Camioneta":
    Total=Total+300


#Vehículo

def calcular_valor(valor):
    val1=valor*0.2
    return val1

TK=float(input("¿Cúantos kilómetros recorres al mes en vehículo personal?\n"))
TK1=calcular_valor(TK)
Total=Total+TK1

#Residuos
RK=float(input("¿Cuántos kilogramos de residuos generas al mes? \n "))
RK1=calcular_valor(RK)
Total=Total+RK1

#Comida

total_carne_consumida = {"res": 0, "pollo": 0, "cerdo": 0, "pescado": 0}
factores_emision = {"res": 27, "pollo": 6.9, "cerdo": 12.1, "pescado": 5}


while True:
    tipo = input("Introduce el tipo de carne que consumes normalmente (res, pollo, cerdo, pescado)\n introduce toda la carne necesaria, cuando termines o si es que no consumes escribe 'salir'\n: ").lower()
    
    if tipo == 'salir':
        break 
    
    if tipo in total_carne_consumida:
        cantidad = float(input(f"Introduce la cantidad de {tipo} consumida en gramos al mes:\n "))
        total_carne_consumida[tipo] += cantidad
    else:
        print("Tipo de carne no válido, intenta de nuevo.")

total_emisiones = 0
for tipo, cantidad in total_carne_consumida.items():
    emisiones = cantidad * factores_emision[tipo] / 1000  
    Total = Total + emisiones
    
#Electrodomésticos

electrodomesticos=[]

while True:
    nombre = input("Introduce el nombre del electrodoméstico que utilizas normalmente \n ve introducendo uno por uno, cuando termines escribe 'salir' para finalizar:\n ").lower()
    
    if nombre == 'salir':
        break  
    
    horas = float(input(f"Introduce el número de horas que usas {nombre} al día: \n"))
    potencia = float(input(f"Introduce la potencia de {nombre} en watts: \n"))
    
    
    electrodomesticos.append([nombre, horas, potencia])


for electrodomestico in electrodomesticos:
    nombre, horas, potencia = electrodomestico
    consumo_diario = horas * potencia / 1000  
    consumo_total=consumo_diario*30
    Total += consumo_total


#cálculo de arboles
Total2=Total*12
arboles=Total2//30



print(f"Tomando en cuenta SOLO tus hábitos anteriores produces aproximadamente {Total2} kg de CO2 al año")
print(f"Lo que implicaría el plantar al menos {arboles} árboles para cubrir tu huella de solo esos hábitos")


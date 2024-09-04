print("¿Cuál es tu huella de carbono?, ¿Cuántos aárboles necesitarías plantar para cubrirla?, ¡Vamos a descubrirla!")
print("Contesta las siguiente preguntas")

Total=0.0


luzm=float(input("¿Cúantos KwH consumes al mes?"))
Total=luzm*0.5

FR=float(input("Qué porcentaje de tu electricidad proviene de fuentes renovables? (INDIQUE CON UN PORCENTAJE DE 0% AL 100%")) 
if FR==0 :
    Total=Total*10
elif FR==100:
    Total=0
else:
    FRT=FR/100
    FRT1=Total*FRT
    Total=Total-FRT1

#GAS

TP=input("Cúal medio de transporte usas normalmente? (Bicicleta, Caminar, transporte público, Automóvil(Gasolina diesel), Motocicleta, Camioneta")
if TP=="bicicleta" or "caminar":
    Total=Total+0
if TP=="transporte público":
    Total=Total+100
if TP=="Motocicleta":
    Total=Total+250
if TP=="Camioneta":
    Total=Total+300



def calcular_valor(valor):
    val1=valor*0.2
    return val1

TK=float(input("¿Cúantos kilómetros recorres al año n vehículo personal"))
TK1=calcular_valor(TK)
Total=Total+TK1

RK=float(input("¿Cuántos kilogramos de residuos generas al mes?  "))
RK1=calcular_valor(RK)
Total=Total+RK1

print(Total)



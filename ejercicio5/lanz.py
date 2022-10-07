import vehiculo
Carlos_coche=vehiculo.coche("verde",6,200,1700)
Carlos_bicicleta=vehiculo.bicicleta("rojo",5,"deportiva")
Carlos_camion=vehiculo.camion("negro",7,1800)
Carlos_motocicleta=vehiculo.motocicleta("amarillo",3,210,700)
Carlos_vehiculos=[Carlos_coche,Carlos_camion,Carlos_bicicleta,Carlos_motocicleta]

def catal(lista):
    for vehiculo in lista:
        print(vehiculo.__str__())

def catal2(lista,ruedas):
    lista2=[]
    for vehiculo in lista:
        if vehiculo.get_ruedas()==ruedas:
            lista2.append(vehiculo)
    return f"Hemos encontrado{len(lista2)} vehiculos con {ruedas} ruedas"


def menu():
    print("Bienvenido al catálogo de vehículos")
    print("Enseñar vehículos")
    print("1.Enséñame los vehículos de dos ruedas")
    print("2.Enséñame los vehículos de cuatro ruedas")
    print("3.Enséñame los vehículos de seis ruedas")
    print("Salir del catálogo")

r=int(input("Elige la opción que desees."))
if r==1:
    catal(Carlos_vehiculos)
elif r==2:
    print(catal2(Carlos_vehiculos,2))
elif r==3:
    print(catal2(Carlos_vehiculos,4))
elif r==4:
    print(catal2(Carlos_vehiculos,6))
elif r==5:
    print("Que tenga un buen dia")
else:
    print("La opción que has elegido no es válida")
    menu()





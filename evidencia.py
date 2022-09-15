import random

while True:
    print("Bienvenido a Andor, conferencias y reuniones")
    print("********************************************")
    print("¿Que opcion deseas realizar?")
    print("1) Registrar una reservacion")
    print("2) Editar mi reservacion")
    print("3) Consultar reservaciones")
    print("4) Registrar un nuevo cliente")
    print("5) Registrar una sala")
    print("6) Salir")

    respuesta = input("indique su opcion deseada:  ")
    
    respuesta_int = int(respuesta)
    
    if respuesta_int == 1:
        lista = []

      
        print("Ingresa ID del cliente")
        idd = input()
        lista.append(idd)

        print("Ingresa ID de la sala")
        ids = input()
        lista.append(ids)
        
        print("Ingresa nombre de evento")
        xxt = input()
        lista.append(xxt)
        
        print("Ingresa la fecha del evento")
        fechh = input()
        lista.append(fechh)
        
        print("Ingresa turno")
        tturn = input()
        lista.append(tturn)
        
        clvr = random.randrange(99)
        lista.append(clvr)
        
        print("Gracias por reservar, tu numero de reservacion es: ", clvr)
    
    
    elif respuesta_int == 2:
            print(lista)
            
            lista[3] = input("Ingresa nueva fecha")
            
            print("Lista actualizada")
            print(lista)
            
    elif respuesta_int == 3:
            print("Mostrar Reservaciones")
            print("Id cliente/Id sala/Nombre evento/Fecha/Turno/Id reservacion")
            print(lista)
            
    elif respuesta_int == 4:
            print("Hola, ingresa tu nombre para continuar")
            nbr = input()
            
            print(f"Bienvenido {nbr}, gracias por elegir nuestros servicios, a continuacion, seguiremos con tu registro")
            
            print("Ingresa tu nombre completo")
            noom = input()
            
            clvc = random.randrange(99)
            
            print("Gracias por ser parte de nuestra familia, tu ID como cliente es: ", clvc)
            
    elif respuesta_int == 5:
            print("******** Registro de salas ********")
            
            print("***Ingresa el nombre de la sala***")
            nmbs = input()
            
            print("Ingresa el cupo de la sala")
            cum = input()
            
            clvs = random.randrange(9999)
            
            print("Se registro la sala correctamente, el ID de la sala es: ", clvs)
            
    elif respuesta_int == 6:
        print("Gracias por su preferencia, los esperamos de nuevo")
        exit()
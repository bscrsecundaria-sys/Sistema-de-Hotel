#SISTEMA HOTELERO - Archivo principal (main.py)
#Controla el flujo principal del programa

#Importación de módulos
from Modulos.clientes import Cliente
from Modulos.habitaciones import Habitacion
from Modulos.reservas import Reserva
from Modulos.pagos import Pago

#Listas globales donde se almacenan las instancias
clientes = []       # Lista de objetos Cliente
habitaciones = []   # Lista de objetos Habitacion
reservas = []       # Lista de objetos Reserva
pagos = []          # Lista de objetos Pago

#Menú iterativo principal del sistema
while True:
    # Encabezado visual del menú
    print("")
    print("=" * 40)
    print("SISTEMA HOTELERO")
    print("1. Registrar cliente")
    print("2. Registrar nueva habitación")
    print("3. Mostrar habitaciones disponibles")
    print("4. Crear reserva")
    print("5. Consultar reservas de un cliente")
    print("6. Registrar pago")
    print("7. Consultar pagos")
    print("8. Finalizar reserva")
    print("9. Salir")
    print("=" * 40)

    # Solicita la opción al usuario
    opcion = input("\n- Qué opción deseas realizar: ").strip()

    #1: Registrar un nuevo cliente
    if opcion == "1":
        Cliente.registrar_cliente(clientes)

    #2: Registrar una nueva habitación
    elif opcion == "2":
        Habitacion.registrar_habitacion(habitaciones)

    #3: Mostrar todas las habitaciones disponibles
    elif opcion == "3":
        Habitacion.mostrar_disponibles(habitaciones)

    #4: Crear una nueva reserva
    elif opcion == "4":
        Reserva.crear_reserva(clientes, habitaciones, reservas)

    #5: Consultar reservas asociadas a un cliente
    elif opcion == "5":
        if not reservas:  # Validación: si no hay reservas registradas
            print("No existen reservas registradas.")
            continue
        Reserva.consultar_reservas_cliente(reservas)

    #6: Registrar un pago asociado a una reserva
    elif opcion == "6":
        Pago.registrar_pago(pagos, reservas)

    #7: Consultar pagos registrados
    elif opcion == "7":
        if not pagos:  # Validación: si no hay pagos realizados
            print("No hay pagos registrados.")
            continue
        # Muestra cada pago registrado
        for pago in pagos:
            print(pago)

    #8: Finalizar una reserva activa
    elif opcion == "8":
        Reserva.finalizar_reserva(reservas, habitaciones)

    #9: Salir del sistema
    elif opcion == "9":
        print("Saliendo del sistema...")
        break

    #OPCIÓN NO VÁLIDA
    else:
        print("Opción no válida. Ingrese una opción válida.")
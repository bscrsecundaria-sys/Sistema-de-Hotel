#Importacion de modulos
from Modulos.clientes import Cliente
from Modulos.habitaciones import Habitacion
from Modulos.reservas import Reserva
from Modulos.pagos import Pago

# Listas globales
clientes = []
habitaciones = []
reservas = []
pagos = []

#Menu Iterativo
while True:
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

    opcion = input("\n- Que opcion deseas realizar: ").strip()

    if opcion == "1":
        Cliente.registrar_cliente(clientes)

    elif opcion == "2":
        Habitacion.registrar_habitacion(habitaciones)

    elif opcion == "3":
        Habitacion.mostrar_disponibles(habitaciones)

    elif opcion == "4":
        Reserva.crear_reserva(clientes, habitaciones, reservas)

    elif opcion == "5":
        if not reservas:
            print("No existen reservas registradas.")
            continue
        Reserva.consultar_reservas_cliente(reservas)

    elif opcion == "6":
        if not reservas:
            print("No hay reservas para registrar pagos.")
            continue
        Pago.registrar_pago(pagos, reservas)

    elif opcion == "7":
        if not pagos:
            print("No hay pagos registrados.")
            continue
        for p in pagos:
            print(p)

    elif opcion == "8":
        if not reservas:
            print("No hay reservas activas para finalizar.")
            continue
        Reserva.finalizar_reserva(reservas, habitaciones)

    elif opcion == "9":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida. Ingrese una opcion valida.")
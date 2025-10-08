from Modulos.clientes import Cliente
from Modulos.habitaciones import Habitacion
from Modulos.reservas import Reserva
from Modulos.pagos import Pago
 
#Listas globales
clientes = []
habitaciones = []
reservas = []
pagos = []

#Menú principal
while True:
    print("\nSISTEMA HOTELERO - MENÚ PRINCIPAL")
    print("1. Registrar cliente")
    print("2. Registrar nueva habitación")
    print("3. Mostrar habitaciones disponibles")
    print("4. Crear reserva")
    print("5. Consultar reservas de un cliente")
    print("6. Registrar pago")
    print("7. Consultar pagos")
    print("8. Finalizar reserva")
    print("9. Salir")

    opcion = input("\nSeleccione una opción: ")
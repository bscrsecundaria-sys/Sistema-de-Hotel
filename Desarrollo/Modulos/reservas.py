class Reserva:
    # Día 1:
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias
        self.total = dias * habitacion.tarifa
        self.pagada = False

    # Día 2:
    def __str__(self):
        estado = "Pagada" if self.pagada else "Pendiente"
        return f"Reserva de {self.cliente.nombre} - Habitación {self.habitacion.numero} - Días: {self.dias} - Total: ${self.total} ({estado})"

    # Crear nueva reserva
    def crear_reserva(lista_clientes, lista_habitaciones, lista_reservas):
        print("\nCrear nueva reserva")

        if not lista_clientes:
            print("No hay clientes registrados.")
            return
        if not lista_habitaciones:
            print("No hay habitaciones registradas.")
            return

        print("\nClientes registrados:")
        for i, c in enumerate(lista_clientes):
            print(f"{i+1}. {c}")

        idx_cliente = int(input("Seleccione el cliente: ")) - 1
        if idx_cliente < 0 or idx_cliente >= len(lista_clientes):
            print("Selección inválida.")
            return
        cliente = lista_clientes[idx_cliente]

        disponibles = [h for h in lista_habitaciones if h.esta_disponible()]
        if not disponibles:
            print("No hay habitaciones disponibles.")
            return

        print("\nHabitaciones disponibles:")
        for i, h in enumerate(disponibles):
            print(f"{i+1}. {h}")

        idx_hab = int(input("Seleccione una habitación: ")) - 1
        if idx_hab < 0 or idx_hab >= len(disponibles):
            print("Selección inválida.")
            return
        habitacion = disponibles[idx_hab]

        dias = int(input("Cantidad de días de la reserva: "))
        nueva_reserva = Reserva(cliente, habitacion, dias)
        habitacion.ocupar()
        lista_reservas.append(nueva_reserva)
        print(f"\nReserva creada correctamente para {cliente.nombre}.")

    # Consultar reservas de un cliente
    def consultar_reservas_cliente(lista_reservas):
        doc = input("Ingrese el documento del cliente: ")
        encontradas = [r for r in lista_reservas if r.cliente.documento == doc]
        if not encontradas:
            print("No se encontraron reservas para ese cliente.")
            return
        print("\nReservas encontradas:")
        for r in encontradas:
            print(r)

    # Finalizar reserva
    def finalizar_reserva(lista_reservas, lista_habitaciones):
        print("\nFinalizar reserva")

        if not lista_reservas:
            print("No hay reservas activas.")
            return

        for i, r in enumerate(lista_reservas):
            print(f"{i+1}. {r}")

        idx = int(input("Seleccione la reserva a finalizar: ")) - 1
        if idx < 0 or idx >= len(lista_reservas):
            print("Selección inválida.")
            return

        reserva = lista_reservas[idx]
        reserva.habitacion.liberar()
        lista_reservas.remove(reserva)
        print(f"Reserva finalizada. \nLa Habitación {reserva.habitacion.numero} ahora se encuentra disponible.")
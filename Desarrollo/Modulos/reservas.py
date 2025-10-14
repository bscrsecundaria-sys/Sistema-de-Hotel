class Reserva:
    # Día 1: Constructor
    def init(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias
        self.total = dias * habitacion.tarifa
        self.pagada = False

    # Día 2: Representación en texto
    def str(self):
        estado = "Pagada" if self.pagada else "Pendiente"
        return (f"Reserva de {self.cliente.nombre} - Habitación {self.habitacion.numero} "
                f"- Días: {self.dias} - Total: ${self.total} ({estado})")

    # Crear nueva reserva
    def crear_reserva(lista_clientes, lista_habitaciones, lista_reservas):
        print("\nCREAR NUEVA RESERVA")

        if not lista_clientes:
            print("No hay clientes registrados.")
            return
        if not lista_habitaciones:
            print("No hay habitaciones registradas.")
            return

        # Mostrar lista de clientes
        print("\nClientes registrados:")
        for numero_cliente, cliente in enumerate(lista_clientes, start=1):
            print(f"{numero_cliente}. {cliente}")

        # Selección del cliente
        seleccion_cliente = int(input("Seleccione el número del cliente: ")) - 1
        if seleccion_cliente < 0 or seleccion_cliente >= len(lista_clientes):
            print("Selección inválida.")
            return
        cliente_seleccionado = lista_clientes[seleccion_cliente]

        # Filtrar habitaciones disponibles
        habitaciones_disponibles = [h for h in lista_habitaciones if h.esta_disponible()]
        if not habitaciones_disponibles:
            print("No hay habitaciones disponibles.")
            return

        # Mostrar habitaciones disponibles
        print("\nHabitaciones disponibles:")
        for numero_habitacion, habitacion in enumerate(habitaciones_disponibles, start=1):
            print(f"{numero_habitacion}. {habitacion}")

        # Selección de habitación
        seleccion_habitacion = int(input("Seleccione el número de habitación: ")) - 1
        if seleccion_habitacion < 0 or seleccion_habitacion >= len(habitaciones_disponibles):
            print("Selección inválida.")
            return
        habitacion_seleccionada = habitaciones_disponibles[seleccion_habitacion]

        # Días de reserva
        dias_reserva = int(input("Cantidad de días de la reserva: "))
        nueva_reserva = Reserva(cliente_seleccionado, habitacion_seleccionada, dias_reserva)
        habitacion_seleccionada.ocupar()
        lista_reservas.append(nueva_reserva)

        print(f"\nReserva creada correctamente para {cliente_seleccionado.nombre}.")

    # Consultar reservas de un cliente
    def consultar_reservas_cliente(lista_reservas):
        documento = input("Ingrese el documento del cliente: ")
        reservas_cliente = [r for r in lista_reservas if r.cliente.documento == documento]

        if not reservas_cliente:
            print("No se encontraron reservas para ese cliente.")
            return

        print("\nReservas encontradas:")
        for reserva in reservas_cliente:
            print(reserva)

    # Finalizar reserva
    def finalizar_reserva(lista_reservas, lista_habitaciones):
        print("\nFINALIZAR RESERVA")

        if not lista_reservas:
            print("No hay reservas activas.")
            return

        # Mostrar reservas activas
        for numero_reserva, reserva in enumerate(lista_reservas, start=1):
            print(f"{numero_reserva}. {reserva}")

        # Selección de reserva
        seleccion_reserva = int(input("Seleccione el número de reserva a finalizar: ")) - 1
        if seleccion_reserva < 0 or seleccion_reserva >= len(lista_reservas):
            print("Selección inválida.")
            return

        reserva_finalizada = lista_reservas[seleccion_reserva]
        reserva_finalizada.habitacion.liberar()
        lista_reservas.remove(reserva_finalizada)

        print(f"Reserva finalizada. "
              f"La habitación {reserva_finalizada.habitacion.numero} ahora está disponible.")
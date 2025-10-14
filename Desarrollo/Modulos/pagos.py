class Pago:
    # Día 1: Constructor
    def init(self, reserva, metodo, monto):
        self.reserva = reserva
        self.metodo = metodo
        self.monto = monto

    def str(self):
        return f"Pago de ${self.monto} - Método: {self.metodo} - Cliente: {self.reserva.cliente.nombre}"

    # Día 2: Registrar pago
    def registrar_pago(lista_pagos, lista_reservas):
        print("\n--- REGISTRAR PAGO ---")

        if not lista_reservas:
            print("No hay reservas registradas.")
            return

        # Mostrar reservas pendientes de pago
        print("\nReservas disponibles para pago:")
        for numero_reserva, reserva in enumerate(lista_reservas, start=1):
            print(f"{numero_reserva}. {reserva}")

        # Seleccionar reserva
        seleccion_reserva = int(input("Seleccione el número de la reserva a pagar: ")) - 1
        if seleccion_reserva < 0 or seleccion_reserva >= len(lista_reservas):
            print("Selección inválida.")
            return

        reserva_seleccionada = lista_reservas[seleccion_reserva]
        if reserva_seleccionada.pagada:
            print("Esta reserva ya fue pagada.")
            return

        #Dia 3: Facturacion de pagos
        # Seleccionar método de pago
        print("\nMétodos de pago disponibles: efectivo, tarjeta, transferencia, PayPal")
        metodo_pago = input("Método de pago: ").lower()
        if metodo_pago not in ["efectivo", "tarjeta", "transferencia", "paypal"]:
            print("El método de pago es inválido.")
            return

        # Ingresar monto
        print(f"Total a pagar: ${reserva_seleccionada.total}")
        try:
            monto_pagado = float(input("Monto pagado: "))
        except ValueError:
            print("Debe ingresar un valor numérico.")
            return

        if monto_pagado < reserva_seleccionada.total:
            print("El monto pagado es insuficiente.")
            return

        # Registrar pago
        reserva_seleccionada.pagada = True
        nuevo_pago = Pago(reserva_seleccionada, metodo_pago, monto_pagado)
        lista_pagos.append(nuevo_pago)
        print(f"\nPago registrado exitosamente para {reserva_seleccionada.cliente.nombre}.")
class Pago:
    #Dia 1:
    def __init__(self, reserva, metodo, monto):
        self.reserva = reserva
        self.metodo = metodo
        self.monto = monto

    def __str__(self):
        return f"Pago de ${self.monto} - Método: {self.metodo} - Cliente: {self.reserva.cliente.nombre}"

    #Dia 2:
    def registrar_pago(lista_pagos, reservas):
        print("\nRegistrar pago")
        if not reservas:
            print("No hay reservas registradas.")
            return

        for i, r in enumerate(reservas):
            print(f"{i+1}. {r}")

        idx = int(input("Seleccione la reserva a pagar: ")) - 1
        if idx < 0 or idx >= len(reservas):
            print("Selección inválida.")
            return
        
        #Dia 3:
        reserva = reservas[idx]
        if reserva.pagada:
            print("Esta reserva ya fue pagada.")
            return

        print("\nMétodos de pago disponibles: efectivo, tarjeta, transferencia, PayPal")
        metodo = input("Método de pago: ").lower()
        if metodo not in ["efectivo", "tarjeta", "transferencia", "paypal"]:
            print("El método de pago es inválido.")
            return

        print(f"Total a pagar: ${reserva.total}")
        monto = float(input("Monto pagado: "))
        if monto < reserva.total:
            print("El monto pagado es insuficiente.")
            return

        reserva.pagada = True
        nuevo_pago = Pago(reserva, metodo, monto)
        lista_pagos.append(nuevo_pago)
        print("\nEl pago fue registrado exitosamente.")
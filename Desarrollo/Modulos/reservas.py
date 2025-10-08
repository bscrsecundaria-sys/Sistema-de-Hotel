class Reserva:
    #Día 1: 
    def _init_(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias
        self.total = dias * habitacion.tarifa
        self.pagada = False

    #Día 2:
    def _str_(self):
        estado_pago = "Pagada" if self.pagada else "Pendiente"
        return f"Reserva de {self.cliente.nombre} - Habitación {self.habitacion.numero} - Días: {self.dias} - Total: ${self.total} ({estado_pago})"

    #Día 3:
    def finalizar_reserva(self):
        self.habitacion.liberar()
        print(f"Reserva finalizada para {self.cliente.nombre}. Habitación {self.habitacion.numero} liberada.")
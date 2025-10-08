class Habitacion:
    #Dia 1:
    def __init__(self, numero, tipo, tarifa, estado="disponible"):
        self.numero = numero
        self.tipo = tipo
        self.tarifa = tarifa
        self.estado = estado

    def __str__(self):
        return f"Habitación {self.numero} | Tipo: {self.tipo} | Tarifa: ${self.tarifa} | Estado: {self.estado}"

    def esta_disponible(self):
        return self.estado == "disponible"

    #Dia 2:
    def ocupar(self):
        self.estado = "ocupada"

    def liberar(self):
        self.estado = "disponible"

    #Dia 3:
    def registrar_habitacion(lista_habitaciones):
        print("\nRegistrar nueva habitación")
        numero = int(input("Número de habitación: "))
        if any(h.numero == numero for h in lista_habitaciones):
            print("Ya existe una habitación con ese número.")
            return

        tipo = input("Tipo de habitación (Sencilla/Doble/Suite): ")
        tarifa = float(input("Tarifa por noche: "))
        nueva = Habitacion(numero, tipo, tarifa)
        lista_habitaciones.append(nueva)
        print(f"\nHabitación {numero} registrada exitosamente.")
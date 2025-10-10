class Habitacion:
    # Día 1:
    def _init_(self, numero, tipo, tarifa, estado="disponible"):
        self.numero = numero
        self.tipo = tipo
        self.tarifa = tarifa
        self.estado = estado

    def _str_(self):
        return f"Habitación {self.numero} | Tipo: {self.tipo} | Tarifa: ${self.tarifa} | Estado: {self.estado}"

    def esta_disponible(self):
        return self.estado == "disponible"

    # Día 2:
    def ocupar(self):
        self.estado = "ocupada"

    def liberar(self):
        self.estado = "disponible"

    # Día 3:
    def registrar_habitacion(lista_habitaciones):
        print("\nRegistrar nueva habitación")
        numero = int(input("Número de habitación: "))

        for h in lista_habitaciones:
            if h.numero == numero:
                print("Ya existe una habitación con ese número.")
                return

        tipo = input("Tipo de habitación (Sencilla/Doble/Suite): ")
        tarifa = float(input("Tarifa por noche: "))

        nueva = Habitacion(numero, tipo, tarifa)
        lista_habitaciones.append(nueva)
        print(f"\nHabitación {numero} registrada exitosamente.")

    #Metodo para mostrar disponibles
    def mostrar_disponibles(lista_habitaciones):
        print("\nHabitaciones disponibles:")
        disponibles = [h for h in lista_habitaciones if h.esta_disponible()]
        if not disponibles:
            print("No hay habitaciones disponibles.")
            return
        for h in disponibles:
            print(h)
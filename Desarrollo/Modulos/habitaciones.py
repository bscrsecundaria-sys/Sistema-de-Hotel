class Habitacion:
    #Dia 1: Constructor
    # Inicializa una habitación con número, tipo, tarifa y estado (por defecto "disponible").
    def _init_(self, numero, tipo, tarifa, estado="disponible"):
        self.numero = numero
        self.tipo = tipo
        self.tarifa = tarifa
        self.estado = estado

    # Representación en texto de la habitación al imprimirla.
    def _str_(self):
        return f"Habitación {self.numero} | Tipo: {self.tipo} | Tarifa: ${self.tarifa} | Estado: {self.estado}"

    # Verifica si la habitación está disponible para reservar.
    def esta_disponible(self):
        return self.estado == "disponible"

    #Dia 2: Metodos de estado
    # Marca la habitación como ocupada.
    def ocupar(self):
        self.estado = "ocupada"

    # Libera la habitación (la marca nuevamente como disponible).
    def liberar(self):
        self.estado = "disponible"

    #Día 3: Registro de habitaciones
    # Permite registrar una nueva habitación dentro de la lista global de habitaciones.
    def registrar_habitacion(lista_habitaciones):
        print("\nRegistrar nueva habitación")

        # Solicita el número de habitación y valida si ya existe.
        numero = int(input("Número de habitación: "))
        for h in lista_habitaciones:
            if h.numero == numero:
                print("Ya existe una habitación con el numero ingresado.")
                return

        # Solicita los datos básicos de la habitación (tipo y tarifa).
        tipo = input("Tipo de habitación (Sencilla/Doble/Suite): ")
        tarifa = float(input("Tarifa por noche: "))

        # Crea la instancia y la agrega a la lista global.
        nueva = Habitacion(numero, tipo, tarifa)
        lista_habitaciones.append(nueva)
        print(f"\nLa habitación {numero} fue registrada exitosamente.")

    # ------------------ Mostrar habitaciones disponibles ------------------
    # Muestra todas las habitaciones que estén marcadas como disponibles.
    def mostrar_disponibles(lista_habitaciones):
        print("\nHabitaciones disponibles:")
        disponibles = [h for h in lista_habitaciones if h.esta_disponible()]

        # Si no hay habitaciones disponibles, se muestra un mensaje de aviso.
        if not disponibles:
            print("No hay habitaciones disponibles.")
            return

        # Imprime cada habitación disponible en la lista.
        for h in disponibles:
            print(h)
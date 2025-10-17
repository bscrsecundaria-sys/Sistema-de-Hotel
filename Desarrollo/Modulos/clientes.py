class Cliente:
    # Día 1: Constructor
    # Inicializa un nuevo cliente con su nombre, documento y teléfono.
    def __init__(self, nombre, documento, telefono):
        self.nombre = nombre
        self.documento = documento
        self.telefono = telefono

    # Día 2: Representación en texto
    # Retorna una descripción legible del cliente cuando se imprime el objeto.
    def __str__(self):
        return f"{self.nombre} (D.I: {self.documento}, Cel: {self.telefono})"

    # Día 3: Registro de clientes (con validación de duplicados)
    # Permite registrar un nuevo cliente en la lista global de clientes.
    def registrar_cliente(lista_clientes):
        print("\nREGISTRAR NUEVO CLIENTE")

        # Solicita los datos del cliente
        nombre = input("Nombre del cliente: ").strip()
        documento = input("Documento de identidad: ").strip()
        telefono = input("Teléfono: ").strip()

        # Validar que no exista documento o teléfono repetido
        for cliente in lista_clientes:
            if cliente.documento == documento:
                print(f"\nYa existe un cliente con el documento {documento}.")
                return
            if cliente.telefono == telefono:
                print(f"\nYa existe un cliente con el teléfono {telefono}.")
                return

        # Crear y registrar el cliente
        nuevo = Cliente(nombre, documento, telefono)
        lista_clientes.append(nuevo)

        # Confirmar registro
        print(f"\nEl cliente {nombre} fue registrado correctamente.")

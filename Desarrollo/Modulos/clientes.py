class Cliente:
    #Día 1: Constructor
    # Inicializa un nuevo cliente con su nombre, documento y teléfono.
    def __init__(self, nombre, documento, telefono):
        self.nombre = nombre
        self.documento = documento
        self.telefono = telefono

    #Día 2: Representación en texto
    # Retorna una descripción legible del cliente cuando se imprime el objeto.
    def __str__(self):
        return f"{self.nombre} (D.I: {self.documento}, Cel: {self.telefono})"

    #Día 3: Registro de clientes
    # Permite registrar un nuevo cliente en la lista global de clientes.
    def registrar_cliente(lista_clientes):
        print("\n Registrar nuevo cliente")

        # Solicita los datos del cliente.
        nombre = input("Nombre del cliente: ")
        documento = input("Documento de identidad: ")
        telefono = input("Teléfono: ")

        # Crea la instancia del cliente y la agrega a la lista global.
        nuevo = Cliente(nombre, documento, telefono)
        lista_clientes.append(nuevo)

        # Confirma el registro exitoso.
        print(f"\nEl cliente {nombre} fue registrado correctamente.")
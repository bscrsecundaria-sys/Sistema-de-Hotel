class Cliente:
    #Dia 1:
    def __init__(self, nombre, documento, telefono):
        self.nombre = nombre
        self.documento = documento
        self.telefono = telefono

    #Dia 2:
    def __str__(self):
        return f"{self.nombre} (Doc: {self.documento}, Tel: {self.telefono})"

    #Dia 3: 
    def registrar_cliente(lista_clientes):
        print("\n Registrar nuevo cliente")
        nombre = input("Nombre del cliente: ")
        documento = input("Documento de identidad: ")
        telefono = input("Teléfono: ")
        nuevo = Cliente(nombre, documento, telefono)
        lista_clientes.append(nuevo)
        print(f"\n Cliente {nombre} registrado correctamente.")
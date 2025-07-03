# Clase base
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.__marca = marca  # Atributo privado
        self.__modelo = modelo  # Atributo privado
        self.__anio = anio  # Atributo privado

    def obtener_info(self):
        return f"{self.__marca} {self.__modelo} ({self.__anio})"

    def arrancar(self):
        return "El vehículo está arrancando."

# Clase derivada
class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas):
        super().__init__(marca, modelo, anio)  # Llamada al constructor de la clase base
        self.puertas = puertas  # Atributo público

    def arrancar(self):
        return "El coche está arrancando."

    def obtener_info(self):
        return f"{super().obtener_info()} - Puertas: {self.puertas}"

# Clase derivada
class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo):
        super().__init__(marca, modelo, anio)  # Llamada al constructor de la clase base
        self.tipo = tipo  # Atributo público

    def arrancar(self):
        return "La moto está arrancando."

    def obtener_info(self):
        return f"{super().obtener_info()} - Tipo: {self.tipo}"

# Función para demostrar polimorfismo
def iniciar_vehiculo(vehiculo):
    print(vehiculo.arrancar())
    print(vehiculo.obtener_info())

# Crear instancias de las clases
coche1 = Coche("Toyota", "Corolla", 2020, 4)
moto1 = Moto("Yamaha", "MT-07", 2021, "Deportiva")

# Usar los métodos para demostrar la funcionalidad
iniciar_vehiculo(coche1)
iniciar_vehiculo(moto1)

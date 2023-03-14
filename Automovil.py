from Vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self):
        super().__init__(200)
        self.numero_ruedas = 4

    def moverse(self):
        print("El automóvil se está moviendo...")
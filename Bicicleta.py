from Vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self):
        super().__init__(30)
        self.numero_ruedas = 2

    def moverse(self):
        print("La bicicleta se está moviendo...")
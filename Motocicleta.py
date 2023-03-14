from Vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    def __init__(self):
        super().__init__(150)
        self.numero_ruedas = 2

    def moverse(self):
        print("La motocicleta se está moviendo...")
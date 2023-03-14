from Perro import Perro
from Gato import Gato

animales = [Perro("Firulais"), Gato("Michi"), Perro("Rex"), Gato("Luna")]

# Iteramos sobre la lista de animales e imprimimos su sonido
for animal in animales:
    print(f"{animal.nombre} dice {animal.hacer_sonido()}")
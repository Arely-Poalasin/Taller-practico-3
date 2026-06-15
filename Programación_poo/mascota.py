# Definición de la clase Mascota
class Mascota:

    # Constructor de la clase
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    # Método para mostrar la información de la mascota
    def mostrar_informacion(self):
        print("\n----- INFORMACIÓN DE LA MASCOTA -----")
        print(f"Nombre : {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad   : {self.edad} años")

    # Método para representar un sonido de la mascota
    def hacer_sonido(self):
        if self.especie.lower() == "perro":
            print(f"{self.nombre} dice: ¡Guau guau!")
        elif self.especie.lower() == "gato":
            print(f"{self.nombre} dice: ¡Miau!")
        else:
            print(f"{self.nombre} hace un sonido característico.")
class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")



if __name__ == "__main__":
    # Crear un usuario
    usuario1 = Usuario("Antonio Carvajal", 25)

    
    usuario1.mostrar_datos()
class Coche:
    def __init__(self, marca, velocidad=0):
        self.marca = marca
        self.velocidad = velocidad
    
    def aumentar_velocidad(self, incremento):
        """Aumenta la velocidad del coche"""
        self.velocidad += incremento
        print(f"Velocidad aumentada en {incremento} km/h")
        self.mostrar_velocidad()
    
    def reducir_velocidad(self, decremento):
        """Reduce la velocidad del coche"""
        if self.velocidad - decremento >= 0:
            self.velocidad -= decremento
            print(f"Velocidad reducida en {decremento} km/h")
        else:
            self.velocidad = 0
            print("El coche se ha detenido")
        self.mostrar_velocidad()
    
    def mostrar_velocidad(self):
        """Muestra la velocidad actual del coche"""
        print(f"{self.marca} - Velocidad actual: {self.velocidad} km/h")
    
    def __str__(self):
        return f"Coche: {self.marca}, Velocidad: {self.velocidad} km/h"



if __name__ == "__main__":

    mi_coche = Coche("Chevrolet")
    
    print("=== Estado inicial ===")
    mi_coche.mostrar_velocidad()
    
    print("\n=== Aumentando velocidad ===")
    mi_coche.aumentar_velocidad(30)
    mi_coche.aumentar_velocidad(20)
    
    print("\n=== Reduciendo velocidad ===")
    mi_coche.reducir_velocidad(25)
    mi_coche.reducir_velocidad(30)  
    print("\n=== Información completa ===")
    print(mi_coche)
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def mostrar_area(self):
        area = self.calcular_area()
        print(f"Rectángulo de base {self.base} y altura {self.altura}")
        print(f"Área: {area}")
        return area



if __name__ == "__main__":
 
    rectangulo1 = Rectangulo(7, 3)
    
  
    area = rectangulo1.calcular_area()
    print(f"Área del rectángulo: {area}")
    

    rectangulo1.mostrar_area()
class Estudiante:
    def __init__(self, nombre, calificaciones=None):
        self.nombre = nombre
       
        if calificaciones is None:
            self.calificaciones = []
        else:
            self.calificaciones = calificaciones
    
    def agregar_calificacion(self, calificacion):
        """Agrega una nueva calificación al estudiante"""
        if 0 <= calificacion <= 100:  # Validar rango típico (0-100)
            self.calificaciones.append(calificacion)
            print(f" Calificación {calificacion} agregada para {self.nombre}")
        else:
            print(" Error: La calificación debe estar entre 0 y 100")
    
    def calcular_promedio(self):
        """Calcula el promedio de las calificaciones"""
        if len(self.calificaciones) == 0:
            return 0  # O podríamos lanzar una excepción
        
        suma = sum(self.calificaciones)
        promedio = suma / len(self.calificaciones)
        return round(promedio, 2)  # Redondear a 2 decimales
    
    def obtener_categoria(self):
        """Determina la categoría según el promedio"""
        promedio = self.calcular_promedio()
        
        if promedio >= 90:
            return "Excelente (A)"
        elif promedio >= 80:
            return "Muy Bueno (B)"
        elif promedio >= 70:
            return "Bueno (C)"
        elif promedio >= 60:
            return "Aprobado (D)"
        else:
            return "Reprobado (F)"
    
    def mostrar_informe(self):
        """Muestra un informe completo del estudiante"""
        print(f"\n INFORME ACADÉMICO")
        print(f"Estudiante: {self.nombre}")
        print(f"Calificaciones: {self.calificaciones}")
        print(f"Cantidad de calificaciones: {len(self.calificaciones)}")
        
        if len(self.calificaciones) > 0:
            promedio = self.calcular_promedio()
            print(f"Promedio: {promedio}")
            print(f"Categoría: {self.obtener_categoria()}")
            print(f"Calificación más alta: {max(self.calificaciones)}")
            print(f"Calificación más baja: {min(self.calificaciones)}")
        else:
            print("  No hay calificaciones registradas")
    
    def __str__(self):
        if len(self.calificaciones) == 0:
            return f"Estudiante: {self.nombre} (Sin calificaciones)"
        
        promedio = self.calcular_promedio()
        return f"Estudiante: {self.nombre} | Promedio: {promedio} | Calificaciones: {len(self.calificaciones)}"



if __name__ == "__main__":
    print("=== SISTEMA DE GESTIÓN DE ESTUDIANTES ===\n")
    
    # Crear estudiantes de diferentes formas
    estudiante1 = Estudiante("Antonio Carvajal", [85, 92, 78, 90])
    estudiante2 = Estudiante("Ana García")
    estudiante3 = Estudiante("Luis Rodríguez", [70, 65, 80, 75, 68])
    
    # Mostrar información inicial
    print("Estudiantes creados:")
    print(f"1. {estudiante1}")
    print(f"2. {estudiante2}")
    print(f"3. {estudiante3}")
    
    # Agregar calificaciones
    print("\n=== AGREGANDO CALIFICACIONES ===")
    estudiante2.agregar_calificacion(95)
    estudiante2.agregar_calificacion(88)
    estudiante2.agregar_calificacion(92)
    estudiante2.agregar_calificacion(105)  
    
    # Calcular promedios individualmente
    print("\n=== PROMEDIOS ===")
    print(f"Promedio de {estudiante1.nombre}: {estudiante1.calcular_promedio()}")
    print(f"Promedio de {estudiante2.nombre}: {estudiante2.calcular_promedio()}")
    print(f"Promedio de {estudiante3.nombre}: {estudiante3.calcular_promedio()}")
    
  
    print("\n=== INFORMES COMPLETOS ===")
    estudiante1.mostrar_informe()
    estudiante2.mostrar_informe()
    estudiante3.mostrar_informe()
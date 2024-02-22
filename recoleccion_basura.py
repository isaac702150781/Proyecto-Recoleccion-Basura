class Basurero:
    def __init__(self, capacidad_maxima):
        self.capacidad_maxima = capacidad_maxima
        self.basura_actual = 0
    
    def agregar_basura(self, cantidad):
        if self.basura_actual + cantidad <= self.capacidad_maxima:
            self.basura_actual += cantidad
            print(f"Se agregaron {cantidad} kg de basura al basurero.")
        else:
            print("El basurero está lleno. No se puede agregar más basura.")
    
    def vaciar_basurero(self):
        self.basura_actual = 0
        print("El basurero se ha vaciado completamente.")

# Ejemplo de uso
if __name__ == "__main__":
    basurero = Basurero(capacidad_maxima=100)  # Capacidad máxima de 100 kg
    basurero.agregar_basura(50)  # Agregar 50 kg de basura
    basurero.agregar_basura(70)  # Intentar agregar 70 kg (el basurero está lleno)
    basurero.vaciar_basurero()  # Vaciar el basurero

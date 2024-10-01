from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14159 * (self.raio ** 2)

    def perimetro(self):
        return 2 * 3.14159 * self.raio

circulo = Circulo(5)
print(f"A area do círculo é = {circulo.area()}")
print(f"O perimetro do círculo é = {circulo.area()}")




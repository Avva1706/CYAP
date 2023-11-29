import math
class Circle:
    def __init__(self, rad):
        if rad < 0:
            rad = rad*(-1)
        self.rad = rad
    def area(self):
        return math.pi * self.rad**2
    def dlina(self):
        return math.pi * self.rad * 2
try:
    rad = float(input("Введите радиус круга: "))
    cir = Circle(rad)
    print(f"Площадь круга: {cir.area()}")
    print(f"Длина окружности: {cir.dlina()}")
except ValueError as e:
    print(f"Ошибка: {e}")
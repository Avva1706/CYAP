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
class Rabot:
    def __init__(self, name, staz, stavka, hours, oklad, bonus):
        self.name = name
        self.staz = staz
        self.stavka = stavka
        self.hours = hours
        self.oklad = oklad
        self.bonus = bonus
    def calc_bonus(self):
        if self.staz < 1:
            return 0.01 * self.oklad
        elif self.staz < 3:
            return 0.05 * self.oklad
        elif self.staz < 5:
            return 0.08 * self.oklad
        else:
            return 0.15 * self.oklad
    def zarplata(self):
        zarplata2 = self.hours + self.stavka
        return zarplata2
    def infa(self):
        print("Фамилия: ", self.name)
        print("Стаж(в годах): ", self. staz)
        print("Часовая ставка: ", self.stavka)
        print("Отработанные часы: ", self.hours)
        print("Оклад: ", self.oklad)
        print("Премия: ", self.bonus)
        print("Заработанная плата: ", self.zarplata)
        print("Итого: ", self.calc_bonus)
try:
    rad = float(input("Введите радиус круга: "))
    cir = Circle(rad)
    print(f"Площадь круга: {cir.area()}")
    print(f"Длина окружности: {cir.dlina()}")
except ValueError as e:
    print(f"Ошибка: {e}")
rabotnik = []
for i in range(1):
    print(f"Введите данные для сотрудника {i+1}")
    name = input("Фамилия: ")
    staz = int(input("Стаж(в годах): "))
    stavka = float(input("Часовая ставка: "))
    hours = float(input("Отработанные часы: "))
    oklad = float(input("Оклад: "))
    bonus = Rabot(name, staz, stavka, hours, oklad, 0).calc_bonus()
    rabotnik.append(Rabot(name, staz, stavka, hours, oklad, bonus))
    for Rabot in rabotnik:
        Rabot.infa()
""" Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат. """


class Car:

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0
        self.is_police = False

    def go(self, speed):
        self.speed = speed
        print(f'{self.name.capitalize()} едет со скоростью {self.speed}')

    def stop(self):
        self.speed = 0
        print(f'{self.name.capitalize()} остановилась')

    def turn(self, direction):
        print(f'{self.name.capitalize()} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.name} {self.speed}')

    def __str__(self):
        print(f'{self.speed} {self.name}: {self.speed}')


class TownCar(Car):

    def __init__(self, name, color):
        super().__init__(name, color)
        self.__speed_limit = 60

    def show_speed(self):
        super().show_speed()
        if self.speed > self.__speed_limit:
            print(f'Превышена максимальная скорость на {self.speed - self.__speed_limit}')

class SportCar(Car):

    def __init__(self, name, color):
        super().__init__(name, color)


class WorkCar(Car):

    def __init__(self, name, color):
        super().__init__(name, color)
        self.__speed_limit = 40

    def show_speed(self):
        super().show_speed()
        if self.speed > self.__speed_limit:
            print(f'Превышена максимальная скорость на {self.speed - self.__speed_limit}')


class PoliceCar(Car):

    def __init__(self, name, color):
        super().__init__(name, color)
        self.is_police = True


new_car = Car('volvo', 'красный')
new_car.show_speed()
new_car.go(120)
new_car.turn('направо')
new_car.stop()

pc = PoliceCar('Лада калина', 'серебристая')
print(pc.is_police)

tc = TownCar('Жучок', 'черный')
tc.go(80)
tc.show_speed()

wc = WorkCar('Бычок', 'белый')
wc.go(30)
wc.show_speed()
wc.go(70)
wc.show_speed()

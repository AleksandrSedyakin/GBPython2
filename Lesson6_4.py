class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина, {self.name}, поехала")

    def stop(self):
        print(f"Машина, {self.name}, остановилась")

    def turn(self):
        print(f"Машина, {self.name}, повернула")

    def show_speed(self):
        print(f"Скорость {self.name}, {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        print(f"Скорость {self.name}, {self.speed} км/ч")
        if self.speed > 60:
            print('Превышаете, сударь!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f"Скорость {self.name}, {self.speed} км/ч")
        if self.speed > 40:
            print('Превышаете, сударь!')


class PoliceCar(Car):
    pass


ferrary = SportCar(200, 'red', 'Ferrary', False)

icarus = TownCar(63, 'white', 'Icarus', False)

ford_transit = WorkCar(50, 'black', 'FordTransit', False)

jiguli = PoliceCar(80, 'red-blue', 'Жига-Дрыга', True)

car_container = [ferrary, icarus, ford_transit, jiguli]

for car in car_container:
    car.go()
    if car.is_police == True:
        print('Берегись, ментяры!')
    car.show_speed()
    car.turn()
    car.stop()
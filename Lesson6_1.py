import time

class TrafficLight:
    import time
    def __init__(self):
        self.__color = ['красный', 'желтый', 'зеленый']

    def running(self):
        while True:
            for light in self.__color:
                if light == 'красный':
                    print(f"Горит {light} свет")
                    time.sleep(7)
                elif light == 'желтый':
                    print(f"Горит {light} свет")
                    time.sleep(2)
                else:
                    print(f"Горит {light} свет")
                    time.sleep(10)

my_tr_light = TrafficLight()
my_tr_light.running()


'''
Создать не менее двух дескрипторов для атрибутов классов, которые вы создали ранее в ДЗ.
'''

from time import sleep


class ColorCheck:
    def __init__(self, my_atr):
        self.my_atr = my_atr

    def __set__(self, instance, value):
        if (value != "Red") or (value != "Yllow") or (value != "Green"):
            raise ValueError("Другой цвет!")
        else:
            instance.__dict__[self.my_atr] = value


class TrafficLight:
    __color = None

    def running(time_green):
        i = 1
        time_red = 7
        time_yllow = 2
        while (i > 0):
            print('Красный сигнал светофора')
            sleep(time_red)
            print('Жёлтый сигнал светофора')
            sleep(time_yllow)
            print('Зелёный сигнал светофора')
            sleep(time_green)


a = TrafficLight
a.running(int(input('Введите длительность работы зелёного сигнала светофора :')))

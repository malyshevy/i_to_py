'''
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии(get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:
    name = None
    surname = None
    position = None
    _income = {"wage": None, "bonus": None}


class Position(Worker):
    def get_full_name():
        Worker.name = input('Введите имя : ')
        Worker.surname = input('Введите фамилию : ')

    def get_total_income():
        Worker._income['wage'] = int(input('Введите оклад : '))
        Worker._income['bonus'] = int(input('Введите бонус : '))
        print(f'{Worker.name} {Worker.surname}')
        print(f'Доход с учётом бонуса = {Worker._income["wage"] + Worker._income["bonus"]}')


w = Position
w.get_full_name()
w.get_total_income()

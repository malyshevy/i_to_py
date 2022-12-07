'''
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''
from sys import argv

script_name, first_param, second_param, third_param = argv
print(f'Имя скрипта: {script_name}')
print(f'Выработка в часах: {first_param}')
print(f'Ставка в часах: {second_param}')
print(f'Премия: {third_param}')
try:
    print(f'Заработная плата сотрудника составляет: {int(first_param) * int(second_param) + int(third_param)}')
except:
    print('Вводите числа через пробел')
finally:
    print('Quit')

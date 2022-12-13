'''
Замер времени выполнения 2 х функций из task1_speed
'''
from timeit import timeit
from task1_speed import max_first
from task1_speed import max_sekond

a = timeit("max_first()", globals=globals(), number=10000)
b = timeit("max_sekond()", globals=globals(), number=10000)
print(f'Скорость работы первого скрипта : {a}')
print(f'Скорость работы оптимизированного скрипта : {b}')
print(f"Скорость работы увеличилась в {a / b} раз")

'''Скрипт оптимизировал применением встроенных функций max и list'''
'''
Скорость работы первого скрипта : 0.08777750004082918
Скорость работы оптимизированного скрипта : 0.008902600035071373
Скорость работы увеличилась в 9.859760035836032 раз
'''

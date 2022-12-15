'''
Замер времени выполнения 4 х функций из task1_speed
'''
from timeit import timeit
from task1_speed import max_first
from task1_speed import max_sekond
from task1_speed import rank_first
from task1_speed import rank_seсond

a = timeit("max_first()", globals=globals(), number=10000)
b = timeit("max_sekond()", globals=globals(), number=10000)
print(f'Скорость работы первого скрипта : {a}')
print(f'Скорость работы оптимизированного скрипта : {b}')
print(f"Скорость работы уменьшилась в {a / b} раз \n")

'''Скрипт оптимизировал применением встроенных функций max и list'''
'''
Скорость работы первого скрипта : 0.08777750004082918
Скорость работы оптимизированного скрипта : 0.008902600035071373
Скорость работы уменьшилась в 9.859760035836032 раз
'''
'''Скрипт оптимизировал применением встроенной функции pow'''
c = timeit("rank_first()", globals=globals(), number=10000)
d = timeit("rank_seсond", globals=globals(), number=10000)
print(f'Скорость работы первого скрипта : {c}')
print(f'Скорость работы оптимизированного скрипта : {d}')
print(f"Скорость работы уменьшилась в {c / d} раз")

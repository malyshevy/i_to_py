'''
Замер объёма занимаемой памяти при выполнении 4 х функций из task2
'''
import task2
from memory_profiler import profile

'''Изначальный код'''


@profile()
def run():
    task2.writer


'''
# В код добавлено удаление ссылки на переменную
'''


@profile()
def run_second():
    task2.writer_second



'''Использование памяти идентично согласно отчёта'''

'''Впишите что либо : 1
Впишите что либо : 
Filename: C:\GB\7 Pyton\i_to_py\DZ6\task2.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     7     22.4 MiB     22.4 MiB           1   @profile()
     8                                         def writer():
     9     22.5 MiB      0.0 MiB           2       with open('task1.txt', 'w+') as f_string:
    10     22.5 MiB      0.0 MiB           1           i = 1
    11     22.5 MiB      0.0 MiB           2           while i > 0:
    12     22.5 MiB      0.0 MiB           2               my_string = input('Впишите что либо : ')
    13     22.5 MiB      0.0 MiB           2               if len(list(my_string)) == 0:
    14     22.5 MiB      0.0 MiB           1                   break
    15                                                     else:
    16     22.5 MiB      0.0 MiB           1                   f_string.write(my_string)
    17     22.5 MiB      0.0 MiB           1                   f_string.write('\n')


Впишите что либо : 1
Впишите что либо : 
Filename: C:\GB\7 Pyton\i_to_py\DZ6\task2.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    38     22.5 MiB     22.5 MiB           1   @profile()
    39                                         def writer_second():
    40     22.5 MiB      0.0 MiB           2       with open('task1.txt', 'w+') as f_string:
    41     22.5 MiB      0.0 MiB           1           i = 1
    42     22.5 MiB      0.0 MiB           2           while i > 0:
    43     22.5 MiB      0.0 MiB           2               my_string = input('Впишите что либо : ')
    44     22.5 MiB      0.0 MiB           2               if len(list(my_string)) == 0:
    45     22.5 MiB      0.0 MiB           1                   my_string = None
    46     22.5 MiB      0.0 MiB           1                   del my_string
    47     22.5 MiB      0.0 MiB           1                   break
    48                                                     else:
    49     22.5 MiB      0.0 MiB           1                   f_string.write(my_string)
    50     22.5 MiB      0.0 MiB           1                   f_string.write('\n')
    51     22.5 MiB      0.0 MiB           1                   my_string = None
    52     22.5 MiB      0.0 MiB           1                   del my_string
'''


@profile()
def run():
    task2.my_func(5, -5)

'''
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''
from memory_profiler import profile


@profile()
def writer():
    with open('task1.txt', 'w+') as f_string:
        i = 1
        while i > 0:
            my_string = input('Впишите что либо : ')
            if len(list(my_string)) == 0:
                break
            else:
                f_string.write(my_string)
                f_string.write('\n')


writer()

'''Впишите что либо : 1
Впишите что либо : 
Filename: C:\GB\7 Pyton\i_to_py\DZ6\task2.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     6     22.4 MiB     22.4 MiB           1   @profile()
     7                                         def writer():
     8     22.4 MiB      0.0 MiB           2       with open('task1.txt', 'w+') as f_string:
     9     22.4 MiB      0.0 MiB           1           i = 1
    10     22.4 MiB      0.0 MiB           2           while i > 0:
    11     22.4 MiB      0.0 MiB           2               my_string = input('Впишите что либо : ')
    12     22.4 MiB      0.0 MiB           2               if len(list(my_string)) == 0:
    13     22.4 MiB      0.0 MiB           1                   break
    14                                                     else:
    15     22.4 MiB      0.0 MiB           1                   f_string.write(my_string)
    16     22.4 MiB      0.0 MiB           1                   f_string.write('\n')
'''


@profile()
def writer_second():
    with open('task1.txt', 'w+') as f_string:
        i = 1
        while i > 0:
            my_string = input('Впишите что либо : ')
            if len(list(my_string)) == 0:
                my_string = None
                del my_string
                break
            else:
                f_string.write(my_string)
                f_string.write('\n')
                my_string = None
                del my_string


writer_second()

'''Впишите что либо : 1
Впишите что либо : 
Filename: C:\GB\7 Pyton\i_to_py\DZ6\task2.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     6     22.3 MiB     22.3 MiB           1   @profile()
     7                                         def writer():
     8     22.3 MiB      0.0 MiB           2       with open('task1.txt', 'w+') as f_string:
     9     22.3 MiB      0.0 MiB           1           i = 1
    10     22.3 MiB      0.0 MiB           2           while i > 0:
    11     22.3 MiB      0.0 MiB           2               my_string = input('Впишите что либо : ')
    12     22.3 MiB      0.0 MiB           2               if len(list(my_string)) == 0:
    13     22.3 MiB      0.0 MiB           1                   del my_string
    14     22.3 MiB      0.0 MiB           1                   break
    15                                                     else:
    16     22.3 MiB      0.0 MiB           1                   f_string.write(my_string)
    17     22.3 MiB      0.0 MiB           1                   f_string.write('\n')
    18     22.3 MiB      0.0 MiB           1                   del my_string
'''


@profile()
# Функция возведения в степень
def my_func(x, y):
    '''
    :param x: первое введённое число
    :param y: второе введённое число
    :return: список ответов
    '''
    f = 1  # Переменная со значением 1
    num_ferst = 0
    num_second = f
    num_fry = 0
    if x > 0 and y < 0:
        # Первый вариант решения
        num_ferst = x ** y
        # Второй вариант решения
        i = 0
        while i > y:
            num_second = num_second * x
            i -= f
        num_second = f / num_second
        # Третий вариант решения
        i = f
        num_fry = x
        d = x
        while i < abs(y):
            j = f
            while j < x:
                num_fry += d
                j += f
            d = num_fry
            i += f
        num_fry = f / num_fry
    else:
        print('Введите верные числа...')
        exit()
    del i, d, f, j, x, y
    num_list = [num_ferst, num_second, num_fry]
    print(num_list)


my_func(5, -5)

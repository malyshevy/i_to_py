'''Исходная задача'''
'''
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''

'''Не оптимизированный скрипт '''
def max_first():
    #    string_out = input('Введите целое положительное число : ')
    #    number_out = int(string_out)
    string_out = str(1234567890)
    number_out = int(string_out)
    number_sise = len(string_out)
    if number_out > 0:
        number_max = number_out // (10 ** (number_sise - 1))
        numbers_difference = number_out
        while number_sise > 0:
            if number_max <= (numbers_difference // (10 ** (number_sise - 1))):
                numbers_multipler = numbers_difference // (10 ** (number_sise - 1))
                if number_max == 9:
                    break
                else:
                    number_max = numbers_difference // (10 ** (number_sise - 1))
                    numbers_difference = numbers_difference - (numbers_multipler * (10 ** (number_sise - 1)))
                    number_sise -= 1
            else:
                numbers_multipler = numbers_difference // (10 ** (number_sise - 1))
                numbers_difference = numbers_difference - (numbers_multipler * (10 ** (number_sise - 1)))
                number_sise -= 1
    #        print(f'Самая большая цифра в числе {number_out} = {number_max}')

    else:
        print('Попробуйте ввести целое положительное число при следующем использовании программы')

'''Оптимизированный скрипт'''
'''Скрипт оптимизировал применением встроенных функций max и list'''
def max_sekond():
    string_out = str(1234567890)
    number_sise = max(list(string_out))
    return (number_sise)

'''
Скорость работы первого скрипта : 0.08777750004082918
Скорость работы оптимизированного скрипта : 0.008902600035071373
Скорость работы уменьшилась в 9.859760035836032 раз
'''



def rank_first():
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
        num_list = [num_ferst, num_second, num_fry]
        return num_list

    # Ввод данных
    my_num_ferst = 12
    # int(input('Введите действительное положительное число : '))
    my_num_second = -3
    # int(input('Введите целое отрицательное число : '))
    # Вывод на экран
    my_num_list = my_func(my_num_ferst, my_num_second)
    return my_num_list
    #print(f'Вариант 1 = {my_num_list[0]:.5f}, Вариант 2 = {my_num_list[1]:.5f}, Вариант 3 = {my_num_list[2]:.5f}')


def rank_seсond():
    my_num_ferst = 12
    my_num_second = -3
    return pow(my_num_ferst, my_num_second)


'''
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''
import sys


# Функция ввода номера
def func_input_number():
    '''
    :return: возвращает введённый номер с 1 по 12
    '''
    input_number = input('Введите номер месяца : ')
    if (int(input_number) > 12) or (int(input_number) < 1):
        sys.exit('Вы ввели не верное значение . Попробуйте ещё раз')
    else:
        return (int(input_number))


# Переменная хранящая номер месяца
number_months = func_input_number()


# Функция решения через list
def func_list_rezult(num_months):
    '''
    :param num_months: числовой номер месяца
    :return: возврат значения элемента листа по индексу
    '''
    months_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
    return (months_list[num_months - 1])


# Функция решения через dict
def func_dict_rezult(num_months):
    '''
    :param num_months: числовой номер месяца
    :return: возврат значения элемента словаря по ключу
    '''
    months_dict = dict({
        1: 'зима',
        2: 'зима',
        3: 'весна',
        4: 'весна',
        5: 'весна',
        6: 'лето',
        7: 'лето',
        8: 'лето',
        9: 'осень',
        10: 'осень',
        11: 'осень',
        12: 'зима'})
    return (months_dict[num_months])


print(f'list : {number_months} месяц это {func_list_rezult(number_months)}')
print(f'dict : {number_months} месяц это {func_dict_rezult(number_months)}')

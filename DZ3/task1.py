'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''


# Функция приёма чисел их деления и вывода на экран
def func_input_del(first_num, second_num):
    '''
    :param first_num: первое число
    :param second_num: второе число
    '''
    if first_num == 0 or second_num == 0:
        print('При делении на 0 получается 0. Попробуйте вместо 0 ввести другое число')
    else:
        print(f'{first_num} / {second_num} = {first_num / second_num:.2f}')


# Запрос чисел у пользователя
my_first_num = float(input('Введите первое число : '))
my_second_num = float(input('Введите второе число : '))

# Вызов функции
func_input_del(my_first_num, my_second_num)
func_input_del(my_second_num, my_first_num)

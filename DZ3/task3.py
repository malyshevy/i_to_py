'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''


# Функция нахождения 2х наибольших чисел
def my_func(num_one, num_tu, num_fri):
    '''
    :param num_one: первое число
    :param num_tu: второе число
    :param num_fri: третье число
    :return: сумма двух самых больших чисел
    '''
    list_ferst = [num_one, num_tu, num_fri]
    list_ferst = sorted(list_ferst, reverse=True)
    print(f'Два наибольших аргумента : {list_ferst[0]} , {list_ferst[1]}')
    return list_ferst[0] + list_ferst[1]


# Ввод данных
my_num_one = float(input('Введите первое число : '))
my_num_tu = float(input('Введите второе число : '))
my_num_fri = float(input('Введите третье число : '))
# Вывод результата на экран
print(f'Сумма двух самых больших чисел = {my_func(my_num_one, my_num_tu, my_num_fri):.2f}')

'''
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора *.
Второй — более сложная реализация без оператора *, предусматривающая использование цикла.
'''


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
my_num_ferst = int(input('Введите действительное положительное число : '))
my_num_second = int(input('Введите целое отрицательное число : '))
# Вывод на экран
my_num_list = my_func(my_num_ferst, my_num_second)
print(f'Вариант 1 = {my_num_list[0]:.5f}, Вариант 2 = {my_num_list[1]:.5f}, Вариант 3 = {my_num_list[2]:.5f}')

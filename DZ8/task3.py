'''Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''


class Null:
    def null_out():
        try:
            num_first = float(input('Введи делимое: '))
            num_second = float(input('Введи делитель: '))
            num = num_first / num_second
            return print(f'{num:.2f}')
        except:
            return print('Не дели на ноль !!! Попробуй ещё раз...')

a=Null
a.null_out()

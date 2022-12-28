'''
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''
def big_number(number):
    string_out = number #input('Введите целое положительное число : ')
    number_out = int(string_out)
    number_sise = len(string_out)
    number_max = None
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
        print(f'Самая большая цифра в числе {number_out} = {number_max}')

    else:
        print('Попробуйте ввести целое положительное число при следующем использовании программы')
    return number_max
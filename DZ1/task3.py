'''
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''
string_out = input('Введите число :')
number_out = int(string_out) + int(string_out + string_out) + int(string_out + string_out + string_out)
print(f'{string_out} + {string_out + string_out} + {string_out + string_out + string_out} = {number_out}')

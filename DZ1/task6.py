'''
Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
'''
number_distance_fierst = float(input('Результат спортсмена в первый день (введите длинну дистанции пробежки в первый день) :'))
number_distance_second = float(input('Введите желаемую длинну дистанции пробежки :'))
number_i = 1
if (number_distance_fierst > 0) & (number_distance_second > 0):
    print(f'{number_i} день: {number_distance_fierst:.2f}')
    while number_distance_fierst <= number_distance_second:
        number_distance_fierst = number_distance_fierst + (number_distance_fierst * 0.1)
        number_i += 1
        print(f'{number_i} день: {number_distance_fierst:.2f}')
else:
    print('Введите значение отличное от "0"')
print(f'Ответ: на {number_i} день спортсмен достиг результата - не менее {number_distance_second:.2f}')

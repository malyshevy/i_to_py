'''
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
'''
from random import randint


def generator(list_generator):
    i = 1
    j = 0
    while i < len(list_generator):
        if list_generator[j] < list_generator[i]:
            yield list_generator[i]
            i += 1
            j += 1
        else:
            i += 1
            j += 1


list_generator = [randint(0, 1300) for i in range(0, 13)]
print(list_generator)
for k in generator(list_generator):
    print(k)

'''
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
'''
from random import randint


def generator(list_generator):
    for i in list_generator:
        j = 0
        max = 0
        while j < len(list_generator):
            if i == list_generator[j]:
                max += 1
                j += 1
            else:
                j += 1
        if max > 1:
            continue
        else:
            yield (i)


list_generator = [randint(1, 15) for i in range(0, 15)]
print(list_generator)
new_list = [k for k in generator(list_generator)]
print(new_list)

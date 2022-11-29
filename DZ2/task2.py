'''
Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''
my_list_fierst = list(input('Введите список элементов : '))


# Обмен элементов с индексами 0 и 1, 2 и 3 и т.д.
def func_replacement_list(my_list):
    '''
    :param my_list: список элементов
    :return: возврат изменённого списка элементов
    '''
    if (len(my_list) % 2) > 0:
        size_my_list = len(my_list) - 1
        i = 0
        while i < size_my_list:
            j = None
            j = my_list[i]
            my_list[i] = my_list[i + 1]
            my_list[i + 1] = j
            i += 2
    else:
        size_my_list = len(my_list)
        i = 0
        while i < size_my_list:
            j = None
            j = my_list[i]
            my_list[i] = my_list[i + 1]
            my_list[i + 1] = j
            i += 2
    return (my_list)


print(f'Исходный список элементов : {my_list_fierst}')
print(f'Итоговый список элементов : {func_replacement_list(my_list_fierst)}')

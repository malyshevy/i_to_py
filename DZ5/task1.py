'''
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''
with open('task1.txt', 'w+') as f_string:
    i = 1
    while i > 0:
        my_string = input('Впишите что либо : ')
        if len(list(my_string)) == 0:
            break
        else:
            f_string.write(my_string)
            f_string.write('\n')

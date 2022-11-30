'''
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
'''
my_string = input('Введите несколько слов через пробел : ')
my_list = my_string.split()
i = 0
while i < len(my_list):
    if len(list(my_list[i])) > 9:
        list_first = list(my_list[i])
        list_first = list_first[:10]
        list_first = [str(i) for i in list_first]
        list_second = "".join(list_first)
        print(f'{i + 1} {list_second}')
        i += 1
    else:
        print(f'{i + 1} {my_list[i]}')
        i += 1

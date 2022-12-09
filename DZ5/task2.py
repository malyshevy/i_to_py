'''
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''
with open('task2.txt', 'r') as f_task2:
    size = sum(1 for _ in f_task2)
    print(f'Общее количество строк в файле : {size}')
    f_task2.seek(0)
    i = 1
    while i <= size:
        my_string = f_task2.readline()
        my_list = my_string.split()
        my_numbs = len(my_list)
        print(f'В строке {i} - количество слов : {my_numbs}')
        i +=1

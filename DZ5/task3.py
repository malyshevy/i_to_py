'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
'''
with open('task3.txt', 'r', encoding="utf-8") as f_3:
    size = sum(1 for _ in f_3)
    f_3.seek(0)
    list_f_task3 = []
    i = 0
    while i < size:
        list_f_task3.append(f_3.readline())
        i += 1
    fio = None
    zp = None
    summ = 0
    summ_second = 0
    j = 0
    for i in list_f_task3:
        i = i.split()
        summ = summ + int(i[1])
        if int(i[1]) < 20000:
            zp = (int(i[1]))
            fio = (i[0])
            summ_second = summ_second + zp
            print(f'{fio} : {zp}')
            j = j + 1
    print(f'Средняя величина дохода выбранных сотрудников : {float(summ_second / j)}')
    print(f'Средняя величина дохода всех сотрудников : {float(summ / size)}')

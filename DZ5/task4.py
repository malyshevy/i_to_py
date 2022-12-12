'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''
zamena = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
list_zamena = []
with open('task4.txt', 'r', encoding="utf-8") as task4:
    for i in task4:
        print(i)
        i = i.split(' ', 1)
        list_zamena.append(zamena[i[0]] + '  ' + i[1])
with open('task4_new.txt', 'w+', encoding="utf-8") as task4_new:
    task4_new.writelines(list_zamena)
    task4_new.seek(0)
    for i in task4_new:
        print(i)

'''
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
'''
number_time = int(input('Введите количество секунд :'))
number_hour = number_time // 3600
number_min = (number_time % 3600) // 60
number_sec = number_time % 60
print(f'Введённое количество секунд равно (часов:минут:секунд)= {number_hour}:{number_min}:{number_sec}')
print('Введённое количество секунд равно (часов:минут:секунд)= %d:%d:%d' % (number_hour, number_min, number_sec))


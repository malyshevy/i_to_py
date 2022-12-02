'''
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''


# Функция вывода данных о пользователе на экран
def func_out_user(name, s_name, year_hb, city, email, n_telephone):
    '''
    :param name: Имя
    :param s_name: Фамилия
    :param year_hb: Год рождения
    :param city: Город проживания
    :param email: Email
    :param n_telephone: Номер телефона
    '''
    print(
        f'Имя {name}, '
        f'Фамилия {s_name}, '
        f'Год рождения {year_hb}, '
        f'Город проживания {city}, '
        f'Email {email}, '
        f'Телефон {n_telephone}')


# Ввод данных
my_name = input('Введите имя : ')
my_s_name = input('Введите фамилию :')
my_year_hb = input('Введите год рождения :')
my_city = input('Введите город проживания :')
my_email = input('Введите адрес электронной почты :')
my_n_telephone = input('Введите номер телефона :')
# Вызов функции
func_out_user(n_telephone=my_n_telephone, name=my_name, s_name=my_s_name, year_hb=my_year_hb, city=my_city,
              email=my_email)

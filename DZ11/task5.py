"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import chardet
import subprocess

data_ping = ['ping', 'yandex.ru']
ping = subprocess.Popen(data_ping, stdout=subprocess.PIPE)
for line in ping.stdout:
    result = chardet.detect(line)
    print(line.decode(result['encoding']))
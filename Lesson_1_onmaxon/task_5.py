"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet


def ping(my_list):
    pong = subprocess.Popen(my_list, stdout=subprocess.PIPE)
    for line in pong.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))


ping(['ping', '-c', '3', 'yandex.ru'])
ping(['ping', '-c', '3', 'youtube.com'])

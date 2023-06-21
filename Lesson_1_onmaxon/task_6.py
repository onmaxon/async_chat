"""
Задание 6.

Создать  НЕ программно (вручную) текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».

Принудительно программно открыть файл в формате Unicode и вывести его содержимое.
Что это значит? Это значит, что при чтении файла вы должны явно указать кодировку utf-8
и файл должен открыться у ЛЮБОГО!!! человека при запуске вашего скрипта.

При сдаче задания в папке должен лежать текстовый файл!

Это значит вы должны предусмотреть случай, что вы по дефолту записали файл в cp1251,
а прочитать пытаетесь в utf-8.

Преподаватель будет запускать ваш скрипт и ошибок НЕ ДОЛЖНО появиться!

Подсказки:
--- обратите внимание, что заполнять файл вы можете в любой кодировке
но открыть нужно ИМЕННО!!! в формате Unicode (utf-8)
--- обратите внимание на чтение файла в режиме rb
для последующей переконвертации в нужную кодировку

НАРУШЕНИЕ обозначенных условий - задание не выполнено!!!
"""

from chardet.universaldetector import UniversalDetector


def _get_encoding(filename):
    detector = UniversalDetector()
    with open(filename, 'rb') as fh:
        for line in fh:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    result = detector.result['encoding']
    return result


def open_file(filename):
    with open(filename, encoding=_get_encoding(filename)) as f_n:
        print(f'Кодировка данного файла: {_get_encoding(filename)}\n')
        for el_str in f_n:
            print(el_str, end='')


# open_file('test_file.txt')
# или так
open_file(input('Введите имя файла вместе с расширением: '))


# 2-ой вариант, но он был первым )
# try:
#     with open('test_file.txt', encoding='utf-8') as f_n:
#         for el_str in f_n:
#             print(el_str, end='')
# except UnicodeDecodeError:
#     with open('test_file.txt', encoding='cp1251') as f_n:
#         for el_str in f_n:
#             print(el_str, end='')

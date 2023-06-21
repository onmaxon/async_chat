"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов:
info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров:
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список.

Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.

В этой же функции создать главный список для хранения данных отчета — например,
main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
"""

from chardet import detect
import re
import csv

def get_data():
    main_data = []
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    for i in range(1,4):
        with open(f"info_{i}.txt", 'rb') as file:
            content_bytes = file.read()
        detected = detect(content_bytes)
        encoding = detected['encoding']
        content_text = content_bytes.decode(encoding)
        with open(f"info_{i}.txt", 'w', encoding='utf-8') as file:
            file.write(content_text)
        with open(f"info_{i}.txt", 'r', encoding='utf-8') as file:
            data = file.read()
            os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
            os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])
            os_name_reg = re.compile(r'Название ОС:\s*\S*\s*\S*\s*\S*')
            os_name_list.append(" ".join(os_name_reg.findall(data)[0].split()[3:5]))
            os_code_reg = re.compile(r'Код продукта:\s*\S*')
            os_code_list.append(os_code_reg.findall(data)[0].split()[2])
            os_type_reg = re.compile(r'Тип системы:\s*\S*')
            os_type_list.append(os_type_reg.findall(data)[0].split()[2])
    headers  = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data.append(headers)

    for i in range(3):
        main_data.append([])
        main_data[i + 1].append(i + 1)
        main_data[i + 1].append(os_prod_list[i])
        main_data[i + 1].append(os_name_list[i])
        main_data[i + 1].append(os_code_list[i])
        main_data[i + 1].append(os_type_list[i])

    return main_data

def write_to_csv(name_out_file:str):
    main_data = get_data()
    with open(name_out_file, 'w') as file:
        file_writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        file_writer.writerows(main_data)

write_to_csv('report_task_1.csv')
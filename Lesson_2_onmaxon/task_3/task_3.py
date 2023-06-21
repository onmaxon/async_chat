"""
3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата.
Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число, третьему — вложенный словарь,
где значение каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
"""

import yaml

data_in = {
    'item': ['book', 'ruler', 'блокнот'],
    'quantity': 10,
    'price': {'book': '7\u20ac - 12\u20ac',
              'ruler': '4\u20ac - 5\u20ac',
              'блокнот': '11\u20ac - 15\u20ac'
              }
    }
with open('report_task_3.yaml', 'w', encoding='utf-8')  as file:
    yaml.dump(data_in, file, default_flow_style=False, allow_unicode=True, sort_keys=False)

with open('report_task_3.yaml', 'r', encoding='utf-8') as file:
    data__out = yaml.load(file, Loader=yaml.SafeLoader)

print(data_in == data__out)
